# -*- coding: utf-8 -*-
"""
File-Suffix-Guide Python 示例脚本
测试你的 Python 环境是否正常工作
"""

def main():
    print("=" * 50)
    print("  🎉 File-Suffix-Guide - Python 测试脚本")
    print("=" * 50)
    print()

    # 基本输出
    print("Hello, File-Suffix-Guide!")
    print()

    # 显示 Python 版本
    import sys
    print(f"🐍 Python 版本: {sys.version}")
    print(f"📂 运行平台: {sys.platform}")
    print()

    # 简单计算
    print("🧮 简单计算测试:")
    a, b = 123, 456
    print(f"   {a} + {b} = {a + b}")
    print(f"   {a} × {b} = {a * b}")
    print()

    # 文件操作测试
    print("📁 文件操作测试:")
    try:
        with open("test_output.txt", "w", encoding="utf-8") as f:
            f.write("这是由 test.py 生成的测试文件\n")
            f.write("来自 File-Suffix-Guide 项目\n")
        print("   ✓ 成功创建 test_output.txt")
    except Exception as e:
        print(f"   ✗ 失败: {e}")
    print()

    print("=" * 50)
    print("  ✅ 所有测试完成！Python 环境正常")
    print("=" * 50)


if __name__ == "__main__":
    main()
