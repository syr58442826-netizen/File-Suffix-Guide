# .jsx 文件后缀详解

## 1. 文件定义 & 用途

.jsx 是 **React JSX** 文件的扩展名。JSX 是 JavaScript 的语法扩展，允许你在 JavaScript 代码中直接写类似 HTML 的标签语法。简单来说，它让你用一种"看起来像 HTML"的方式描述 UI 组件，然后通过编译工具（如 Babel）转换成普通的 JavaScript 函数调用。

React 是 Meta（Facebook）开发的流行前端框架，JSX 是 React 生态的核心组成部分。.jsx 文件本质是 JavaScript，只是用了 JSX 语法。

**主要用途：**
- React 前端项目的组件开发
- 单页应用（SPA）构建
- 服务器端渲染（SSR）配合 Next.js 等框架
- React Native 跨平台移动应用
- 组件库和 UI 组件开发

## 2. 适用场景

- 使用 React 开发前端项目
- 组件化 UI 开发（每个组件一个文件）
- 需要丰富的交互和状态管理
- 配合 React Router、Redux、Zustand 等生态库
- React Native 移动端开发

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + React 扩展、Notepad++ | WebStorm（JetBrains）、Sublime Text |
| Mac | [VS Code](https://code.visualstudio.com/) + React 扩展、Vim | WebStorm |
| Linux | [VS Code](https://code.visualstudio.com/) + React 扩展、Vim | WebStorm |

**新手推荐：** VS Code + 安装 ES7+ React/Redux/React-Native snippets 扩展，代码补全和快捷生成非常方便。

## 4. 如何编辑、如何导出

### 环境准备

**安装 Node.js：** 去 [nodejs.org](https://nodejs.org/) 下载 LTS 版安装。验证：`node -v`、`npm -v`

### 如何编辑

**一个简单的 JSX 组件示例：**
```jsx
// Hello.jsx
import React from 'react';

function Hello({ name }) {
  return (
    <div className="hello">
      <h1>你好，{name}！</h1>
      <button onClick={() => alert('点击了！')}>点我</button>
    </div>
  );
}

export default Hello;
```

注意：JSX 中用 `className` 代替 HTML 的 `class`，用 `onClick` 代替 `onclick`，花括号 `{}` 里可以写任意 JavaScript 表达式。

### 如何运行、如何导出

JSX 不能直接在浏览器运行，必须经过编译。

**创建项目（推荐用 Vite）：**
```bash
# 用 Vite 创建 React 项目（默认用 .jsx）
npm create vite@latest my-react-app -- --template react

cd my-react-app
npm install
npm run dev      # 启动开发服务器，访问 http://localhost:5173
```

**如何导出/打包：**
```bash
# 打包发布（产物在 dist/ 目录，纯静态文件）
npm run build

# 预览打包结果
npm run preview
```

打包后的产物是普通的 HTML + JS + CSS，部署到任意 Web 服务器即可。

**手动编译单个文件（了解原理）：**
```bash
# 安装 Babel 命令行工具
npm install -g @babel/cli @babel/preset-react

# 编译单个 .jsx 文件
npx babel Hello.jsx --presets @babel/preset-react --out-file Hello.js
```

## 5. 常见报错与解决

### 问题1：浏览器报错 "SyntaxError: Unexpected token '<'"

**原因：** 浏览器不认识 JSX 语法，需要先编译成普通 JavaScript。

**解决方法：**
1. 确保用 Vite 或 Webpack 等构建工具，不要直接在 HTML 里引入 .jsx 文件
2. 开发时用 `npm run dev` 启动开发服务器，Vite 会自动编译
3. 如果手动引入，确保先经过 Babel 编译

### 问题2：报错 "Element type is invalid -- expected a string but got undefined"

**原因：** 组件 import/export 方式不匹配，或者组件名拼写错误。

**解决方法：**
1. 检查 `export default` 和 `import Hello from './Hello'` 是否匹配
2. 如果是 `export function Hello()`（非默认导出），import 时要用 `import { Hello } from './Hello'`
3. 检查组件名大小写，React 组件名必须大写开头
4. 确认文件路径和扩展名正确

### 问题3：报错 "'React' is not defined" 或 "React is not defined"

**原因：** 使用了 JSX 语法但没有引入 React，或 React 17+ 的自动 JSX 转换未配置。

**解决方法：**
```jsx
// 方法一：在文件顶部引入 React（传统方式）
import React from 'react';

// 方法二：使用 React 17+ 的自动 JSX 转换（Vite 默认支持）
// 确保 babel/preset-react 的 runtime 选项为 "automatic"
// 这种方式不需要手动 import React
```

### 问题4：报错 "Adjacent JSX elements must be wrapped in an enclosing tag"

**原因：** JSX 不允许返回多个并列的根元素。

**解决方法：**
```jsx
// 错误：返回了两个并列元素
function App() {
  return (
    <h1>标题</h1>
    <p>内容</p>  // 报错
  );
}

// 正确方法一：用 Fragment 包裹
function App() {
  return (
    <>
      <h1>标题</h1>
      <p>内容</p>
    </>
  );
}

// 正确方法二：用 div 包裹
function App() {
  return (
    <div>
      <h1>标题</h1>
      <p>内容</p>
    </div>
  );
}
```

---

## 💡 小知识

- JSX 由 Meta（Facebook）团队开发，2013 年随 React 一起开源
- JSX 编译后本质是 `React.createElement()` 函数调用，`<div />` 等价于 `React.createElement('div', null)`
- JSX 不是模板引擎，它是完整的 JavaScript，所有 JavaScript 语法都能直接用
- React 17 引入了自动 JSX 转换，不再需要在每个文件写 `import React`，编译器自动处理

## 🔗 相关链接

- [React 官网](https://react.dev/)
- [React 中文文档](https://zh-hans.react.dev/)
- [Vite 官网](https://vitejs.dev/)
- [Babel 官网](https://babeljs.io/)
- [WebStorm 官网](https://www.jetbrains.com/webstorm/)
