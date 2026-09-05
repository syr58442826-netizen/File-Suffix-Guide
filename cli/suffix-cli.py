#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Suffix Guide - 命令行文件后缀查询工具

功能:
  - 查询后缀详细信息（精确匹配 + 模糊搜索）
  - 分类浏览
  - 随机推荐
  - 统计信息
  - 彩色表格输出（支持 --no-color 禁用）

纯 Python 标准库实现，无需额外依赖。
Python 3.6+ 兼容，跨平台（Windows / Mac / Linux）。
"""

import os
import sys
import json
import random
import argparse
from collections import defaultdict

# ============================================================
# ANSI 颜色支持（Windows 兼容）
# ============================================================

# 颜色代码
COLORS = {
    'reset':     '\033[0m',
    'bold':      '\033[1m',
    'dim':       '\033[2m',
    'red':       '\033[31m',
    'green':     '\033[32m',
    'yellow':    '\033[33m',
    'blue':      '\033[34m',
    'magenta':   '\033[35m',
    'cyan':      '\033[36m',
    'white':     '\033[37m',
    'bg_blue':   '\033[44m',
    'bg_green':  '\033[42m',
    'bg_yellow': '\033[43m',
}

# 全局颜色开关
_use_color = True


def color(text, *color_names):
    """给文本添加颜色"""
    if not _use_color:
        return text
    prefix = ''.join(COLORS.get(c, '') for c in color_names)
    return prefix + text + COLORS['reset']


def init_color():
    """初始化颜色支持（Windows 下启用 ANSI）"""
    global _use_color
    if not _use_color:
        return
    if sys.platform == 'win32':
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            # 启用虚拟终端处理
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            # 如果失败，禁用颜色
            _use_color = False


# ============================================================
# 数据加载
# ============================================================

def get_data_path():
    """获取 data.json 的路径（与脚本同目录）"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, 'data.json')


def load_data():
    """加载后缀数据"""
    data_path = get_data_path()
    if not os.path.exists(data_path):
        print(color(f"错误: 数据文件不存在: {data_path}", 'red', 'bold'))
        print("请确保 data.json 与 suffix-cli.py 在同一目录下。")
        sys.exit(1)
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError as e:
        print(color(f"错误: 数据文件格式损坏: {e}", 'red', 'bold'))
        sys.exit(1)
    except Exception as e:
        print(color(f"错误: 读取数据文件失败: {e}", 'red', 'bold'))
        sys.exit(1)


# ============================================================
# 表格输出工具
# ============================================================

def print_table(headers, rows, col_widths=None):
    """打印表格

    Args:
        headers: 表头列表
        rows: 行数据列表（每行是一个列表）
        col_widths: 每列宽度（可选，自动计算）
    """
    if not rows and not headers:
        return

    # 计算列数
    num_cols = len(headers)

    # 计算每列宽度
    if col_widths is None:
        col_widths = []
        for i in range(num_cols):
            max_w = len(str(headers[i])) if i < len(headers) else 0
            for row in rows:
                if i < len(row):
                    # 中文字符按 2 个宽度计算
                    w = _str_width(str(row[i]))
                    if w > max_w:
                        max_w = w
            col_widths.append(min(max_w + 2, 50))  # 最宽 50

    # 分隔线
    separator = '+' + '+'.join('-' * w for w in col_widths) + '+'

    # 打印表头
    print(separator)
    header_cells = []
    for i, h in enumerate(headers):
        header_cells.append(_pad_str(str(h), col_widths[i]))
    print('|' + '|'.join(color(h, 'bold', 'cyan') for h in header_cells) + '|')
    print(separator)

    # 打印数据行
    for row in rows:
        cells = []
        for i in range(num_cols):
            val = str(row[i]) if i < len(row) else ''
            cells.append(_pad_str(val, col_widths[i]))
        print('|' + '|'.join(cells) + '|')

    print(separator)


def _str_width(s):
    """计算字符串显示宽度（中文字符占 2）"""
    width = 0
    for ch in s:
        if '\u4e00' <= ch <= '\u9fff' or '\u3000' <= ch <= '\u303f':
            width += 2
        else:
            width += 1
    return width


def _pad_str(s, width):
    """将字符串填充到指定宽度"""
    current = _str_width(s)
    if current >= width:
        # 截断
        return s[:width]  # 简单截断
    return s + ' ' * (width - current)


# ============================================================
# 查询功能
# ============================================================

def query_suffix(data, query, search_mode=False):
    """查询后缀

    Args:
        data: 数据列表
        query: 查询词
        search_mode: 是否为搜索模式（模糊搜索）

    Returns:
        匹配结果列表
    """
    # 规范化查询词
    query = query.strip().lower()
    if query.startswith('.'):
        query = query[1:]

    if not query:
        return []

    results = []

    if not search_mode:
        # 精确匹配后缀名
        for item in data:
            if item['suffix'].lower() == query:
                results.append(item)
                break  # 精确匹配只返回一个

        # 如果精确匹配不到，自动转为模糊搜索
        if not results:
            results = _fuzzy_search(data, query)
    else:
        # 搜索模式：模糊搜索
        results = _fuzzy_search(data, query)

    return results


def _fuzzy_search(data, query):
    """模糊搜索：匹配后缀名、中文名、分类、标签"""
    results = []
    query_lower = query.lower()

    for item in data:
        score = 0
        # 后缀名匹配
        suffix_lower = item['suffix'].lower()
        if query_lower in suffix_lower:
            score += 10
            if suffix_lower == query_lower:
                score += 20
        # 中文名匹配（不区分大小写）
        name = item.get('name', '')
        if query_lower in name.lower():
            score += 8
        # 分类匹配（不区分大小写）
        category = item.get('category', '')
        if query_lower in category.lower():
            score += 5
        # 标签匹配（不区分大小写）
        for tag in item.get('tags', []):
            if query_lower in tag.lower():
                score += 3
        # 描述匹配（不区分大小写）
        description = item.get('description', '')
        if query_lower in description.lower():
            score += 1

        if score > 0:
            results.append((score, item))

    # 按分数排序
    results.sort(key=lambda x: x[0], reverse=True)
    return [item for _, item in results]


def print_detail(item):
    """打印单个后缀的详细信息"""
    suffix = item['suffix']
    name = item.get('name', '')
    category = item.get('category', '')
    description = item.get('description', '')
    software = item.get('software', [])
    tags = item.get('tags', [])
    errors = item.get('errors', [])

    # 标题行
    print()
    title = f"  .{suffix}  —  {name}  "
    print(color(title, 'bold', 'white', 'bg_blue'))
    print()

    # 基本信息
    print(color("【基本信息】", 'bold', 'yellow'))
    info_lines = [
        f"  后缀名:   .{suffix}",
        f"  中文名:   {name}",
        f"  所属分类: {category}",
    ]
    if tags:
        info_lines.append(f"  标签:     {' / '.join(color(t, 'green') for t in tags)}")
    for line in info_lines:
        print(line)
    print()

    # 定义/用途
    print(color("【定义 / 用途】", 'bold', 'yellow'))
    if description:
        # 自动换行（简单处理）
        wrapped = _wrap_text(description, 70)
        for line in wrapped:
            print(f"  {line}")
    else:
        print("  （暂无描述）")
    print()

    # 推荐软件
    print(color("【推荐打开软件】", 'bold', 'yellow'))
    if software:
        for i, sw in enumerate(software, 1):
            print(f"  {i}. {sw}")
    else:
        print("  （暂无推荐）")
    print()

    # 常见报错
    if errors:
        print(color("【常见报错】", 'bold', 'yellow'))
        for i, err in enumerate(errors, 1):
            print(f"  {i}. {err}")
        print()

    # 文档路径
    doc_path = item.get('docPath', '')
    if doc_path:
        print(color("【文档位置】", 'bold', 'dim'))
        print(f"  {doc_path}")
        print()


def _wrap_text(text, width):
    """简单的中文文本换行"""
    lines = []
    current = ''
    current_width = 0

    for ch in text:
        ch_width = 2 if '\u4e00' <= ch <= '\u9fff' else 1
        if current_width + ch_width > width:
            lines.append(current)
            current = ch
            current_width = ch_width
        else:
            current += ch
            current_width += ch_width

    if current:
        lines.append(current)
    return lines


# ============================================================
# 分类浏览
# ============================================================

def list_categories(data):
    """列出所有分类"""
    categories = defaultdict(list)
    for item in data:
        cat = item.get('category', '未分类')
        categories[cat].append(item)

    # 按分类名排序
    sorted_cats = sorted(categories.keys())

    print()
    print(color("【文件后缀分类列表】", 'bold', 'cyan'))
    print()

    headers = ['序号', '分类名称', '后缀数量']
    rows = []
    for i, cat in enumerate(sorted_cats, 1):
        count = len(categories[cat])
        rows.append([str(i), cat, str(count)])

    print_table(headers, rows)
    print()
    print(f"共 {len(sorted_cats)} 个分类，{len(data)} 个后缀。")
    print()
    print(color("提示: 使用 -c 分类名 查看该分类下的所有后缀", 'dim'))
    print()


def list_category_items(data, category_name):
    """列出某分类下的所有后缀"""
    # 精确匹配
    items = [item for item in data if item.get('category', '') == category_name]

    # 如果没找到，模糊匹配
    if not items:
        items = [item for item in data
                 if category_name.lower() in item.get('category', '').lower()]

    if not items:
        print()
        print(color(f"未找到分类: {category_name}", 'red'))
        print()
        print("使用 -l 查看所有可用分类。")
        print()
        return

    # 按后缀名排序
    items.sort(key=lambda x: x['suffix'])

    cat_name = items[0].get('category', category_name)
    print()
    print(color(f"【{cat_name}】  共 {len(items)} 个后缀", 'bold', 'cyan'))
    print()

    headers = ['后缀', '中文名', '标签']
    rows = []
    for item in items:
        tags = ', '.join(item.get('tags', []))
        rows.append(['.' + item['suffix'], item.get('name', ''), tags])

    print_table(headers, rows)
    print()


# ============================================================
# 随机推荐
# ============================================================

def random_recommend(data, count=1):
    """随机推荐后缀"""
    if count <= 0:
        count = 1
    if count > len(data):
        count = len(data)

    samples = random.sample(data, count)

    print()
    if count == 1:
        print(color("【随机推荐】", 'bold', 'magenta'))
        print_detail(samples[0])
    else:
        print(color(f"【随机推荐 {count} 个后缀】", 'bold', 'magenta'))
        print()
        headers = ['后缀', '中文名', '分类']
        rows = []
        for item in samples:
            rows.append(['.' + item['suffix'],
                         item.get('name', ''),
                         item.get('category', '')])
        print_table(headers, rows)
        print()
        print(color("提示: 可使用 python suffix-cli.py 后缀名 查看详情", 'dim'))
        print()


# ============================================================
# 统计信息
# ============================================================

def show_stats(data):
    """显示统计信息"""
    total = len(data)

    # 分类统计
    categories = defaultdict(int)
    for item in data:
        cat = item.get('category', '未分类')
        categories[cat] += 1

    # 标签统计
    tag_count = defaultdict(int)
    for item in data:
        for tag in item.get('tags', []):
            tag_count[tag] += 1

    # 有软件推荐的数量
    with_software = sum(1 for item in data if item.get('software'))
    with_errors = sum(1 for item in data if item.get('errors'))
    with_desc = sum(1 for item in data if item.get('description'))

    print()
    print(color("【文件后缀知识库统计】", 'bold', 'green'))
    print()

    # 总览
    print(color("  总览:", 'bold', 'yellow'))
    print(f"    后缀总数:     {total} 个")
    print(f"    分类数量:     {len(categories)} 个")
    print(f"    有描述的:     {with_desc} 个 ({with_desc*100//total}%)")
    print(f"    有软件推荐:   {with_software} 个 ({with_software*100//total}%)")
    print(f"    有报错解答:   {with_errors} 个 ({with_errors*100//total}%)")
    print()

    # 分类排行
    print(color("  分类数量排行:", 'bold', 'yellow'))
    sorted_cats = sorted(categories.items(), key=lambda x: x[1], reverse=True)
    for i, (cat, cnt) in enumerate(sorted_cats[:10], 1):
        bar_len = cnt * 30 // max(categories.values())
        bar = '█' * bar_len
        print(f"    {i:2d}. {cat:<20s} {cnt:3d} 个  {color(bar, 'green')}")
    print()

    # 热门标签
    print(color("  热门标签 TOP 10:", 'bold', 'yellow'))
    sorted_tags = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)
    tag_str = '  '.join(
        color(f"#{tag} ({cnt})", 'cyan')
        for tag, cnt in sorted_tags[:10]
    )
    print(f"    {tag_str}")
    print()


# ============================================================
# 参数解析
# ============================================================

def build_parser():
    """构建命令行参数解析器"""
    parser = argparse.ArgumentParser(
        prog='suffix-cli',
        description='File Suffix Guide - 文件后缀查询工具',
        epilog='示例:\n'
               '  python suffix-cli.py txt          查询 .txt 后缀\n'
               '  python suffix-cli.py python       模糊搜索\n'
               '  python suffix-cli.py -l           列出所有分类\n'
               '  python suffix-cli.py -c 编程       查看分类下的后缀\n'
               '  python suffix-cli.py -r           随机推荐 1 个\n'
               '  python suffix-cli.py --random 5   随机推荐 5 个\n'
               '  python suffix-cli.py --stats      统计信息',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # 位置参数：查询词
    parser.add_argument(
        'query', nargs='?', default=None,
        help='要查询的后缀名或搜索关键词'
    )

    # 搜索模式
    parser.add_argument(
        '-s', '--search', action='store_true',
        help='明确指定搜索模式（模糊搜索名称、分类、标签）'
    )

    # 列出分类
    parser.add_argument(
        '-l', '--list-categories', action='store_true',
        help='列出所有分类'
    )

    # 分类详情
    parser.add_argument(
        '-c', '--category', metavar='分类名',
        help='列出指定分类下的所有后缀'
    )

    # 随机推荐
    parser.add_argument(
        '-r', '--random', nargs='?', const=1, type=int, default=0,
        metavar='N',
        help='随机推荐后缀（不加数量默认1个，如 --random 5 推荐5个）'
    )

    # 统计信息
    parser.add_argument(
        '--stats', action='store_true',
        help='显示统计信息'
    )

    # 禁用颜色
    parser.add_argument(
        '--no-color', action='store_true',
        help='禁用 ANSI 颜色输出'
    )

    return parser


# ============================================================
# 主函数
# ============================================================

def main():
    global _use_color

    parser = build_parser()
    args = parser.parse_args()

    # 处理颜色开关
    if args.no_color:
        _use_color = False

    # 初始化颜色支持
    init_color()

    # 加载数据
    data = load_data()

    try:
        # 统计信息
        if args.stats:
            show_stats(data)
            return

        # 列出分类
        if args.list_categories:
            list_categories(data)
            return

        # 分类详情
        if args.category:
            list_category_items(data, args.category)
            return

        # 随机推荐
        if args.random > 0:
            random_recommend(data, args.random)
            return

        # 查询功能
        if args.query:
            results = query_suffix(data, args.query, search_mode=args.search)

            if not results:
                print()
                print(color(f"未找到与 \"{args.query}\" 相关的后缀", 'red'))
                print()
                print("试试:")
                print("  - 使用 -s 参数进行更广泛的搜索")
                print("  - 使用 -l 查看所有分类")
                print("  - 使用 -r 随机推荐")
                print()
                return

            # 精确匹配（只有一个结果且是精确匹配）：显示详情
            if len(results) == 1 and not args.search:
                print_detail(results[0])
            else:
                # 多个结果：列表展示
                print()
                print(color(f"找到 {len(results)} 个相关结果:", 'bold', 'cyan'))
                print()

                headers = ['后缀', '中文名', '分类', '标签']
                rows = []
                for item in results[:20]:  # 最多显示 20 条
                    tags = ', '.join(item.get('tags', []))
                    rows.append([
                        '.' + item['suffix'],
                        item.get('name', ''),
                        item.get('category', ''),
                        tags
                    ])

                print_table(headers, rows)

                if len(results) > 20:
                    print()
                    print(color(f"  ... 还有 {len(results) - 20} 条结果未显示", 'dim'))

                print()
                print(color("提示: 使用完整后缀名可查看详情，例如: python suffix-cli.py " +
                            results[0]['suffix'], 'dim'))
                print()

            return

        # 没有任何参数：显示欢迎信息
        print_welcome(data)

    except KeyboardInterrupt:
        print()
        print(color("已取消。", 'yellow'))
        sys.exit(0)
    except Exception as e:
        print()
        print(color(f"发生错误: {e}", 'red', 'bold'))
        import traceback
        if '--debug' in sys.argv:
            traceback.print_exc()
        sys.exit(1)


def print_welcome(data):
    """显示欢迎信息"""
    print()
    print(color("╔══════════════════════════════════════════╗", 'bold', 'cyan'))
    print(color("║     File Suffix Guide                   ║", 'bold', 'cyan'))
    print(color("║     文件后缀查询工具 v1.0                ║", 'bold', 'cyan'))
    print(color("╚══════════════════════════════════════════╝", 'bold', 'cyan'))
    print()
    print(f"  收录后缀总数: {color(str(len(data)), 'bold', 'green')} 个")
    print()
    print("  常用命令:")
    print(f"    {color('python suffix-cli.py txt', 'yellow')}        查询 .txt 后缀详情")
    print(f"    {color('python suffix-cli.py -s python', 'yellow')}   搜索与 python 相关的后缀")
    print(f"    {color('python suffix-cli.py -l', 'yellow')}          列出所有分类")
    print(f"    {color('python suffix-cli.py -c 编程', 'yellow')}     查看编程类后缀")
    print(f"    {color('python suffix-cli.py -r', 'yellow')}          随机推荐一个后缀")
    print(f"    {color('python suffix-cli.py --random 5', 'yellow')}   随机推荐 5 个后缀")
    print(f"    {color('python suffix-cli.py --stats', 'yellow')}     查看统计信息")
    print(f"    {color('python suffix-cli.py -h', 'yellow')}          查看完整帮助")
    print()


if __name__ == '__main__':
    main()
