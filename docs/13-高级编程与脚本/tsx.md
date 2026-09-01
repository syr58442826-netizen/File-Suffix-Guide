# .tsx 文件后缀详解

## 1. 文件定义 & 用途

.tsx 是 **React + TypeScript** 的文件后缀。它在 .jsx（JSX 语法）基础上加入了 TypeScript 的静态类型系统，让你在写 React 组件的同时获得类型检查、智能提示和编译时错误发现。

简单来说，.tsx = .jsx + 类型标注。你可以在组件代码中用类似 HTML 的 JSX 语法写 UI，同时用 TypeScript 给 props、state、函数参数等标注类型，编辑器会在你写代码时就提示错误。

**主要用途：**
- React 前端项目的组件开发（带类型安全）
- TypeScript 生态的 React 组件库开发
- 企业级 React 应用（代码量大、多人协作）
- Next.js 等全栈框架的页面开发
- React Native 跨平台移动应用

## 2. 适用场景

- 中大型 React 项目（需要类型保护）
- 需要长期维护、多人协作的前端项目
- 编写可复用的 React 组件库
- 对代码可靠性要求高的场景
- 全栈 React 应用（Next.js）

## 3. 推荐打开软件

| 平台 | 免费软件 | 专业软件 |
|------|----------|----------|
| Windows | [VS Code](https://code.visualstudio.com/) + TypeScript 扩展、Notepad++ | WebStorm（JetBrains）、Sublime Text |
| Mac | [VS Code](https://code.visualstudio.com/) + TypeScript 扩展、Vim | WebStorm |
| Linux | [VS Code](https://code.visualstudio.com/) + TypeScript 扩展、Vim | WebStorm |

**新手推荐：** VS Code（微软自家的产品，TS 支持最好）+ 安装 ES7+ React snippets 扩展。专业开发可用 WebStorm。

## 4. 如何编辑、如何导出

### 环境准备

**安装 Node.js：** 去 [nodejs.org](https://nodejs.org/) 下载 LTS 版安装。

### 如何编辑

**一个带类型标注的 React TSX 组件示例：**
```tsx
// Hello.tsx
import React from 'react';

// 定义 Props 类型
interface HelloProps {
  name: string;
  age?: number;  // 可选属性
}

const Hello: React.FC<HelloProps> = ({ name, age }) => {
  return (
    <div className="hello">
      <h1>你好，{name}！</h1>
      {age && <p>年龄：{age}</p>}
    </div>
  );
};

export default Hello;
```

注意：`interface HelloProps` 定义了组件的属性类型，`React.FC` 是 React 函数组件的类型。`age?` 的问号表示该属性可选。

### 如何运行、如何导出

.tsx 和 .jsx 一样不能直接在浏览器运行，必须经过编译。Vite 在开发时自动编译，打包时把 TSX 编译成普通 JS。

**创建项目：**
```bash
# 用 Vite 创建 React + TypeScript 项目
npm create vite@latest my-react-ts-app -- --template react-ts

cd my-react-ts-app
npm install
npm run dev      # 启动开发服务器，访问 http://localhost:5173
```

**类型检查：**
```bash
# 单独运行类型检查（不生成文件）
npx tsc --noEmit
```

**如何导出/打包：**
```bash
# 打包发布（产物在 dist/ 目录）
npm run build

# 预览打包结果
npm run preview
```

打包后的产物是纯静态 HTML + JS + CSS，类型信息在编译后被擦除，不影响运行性能。

## 5. 常见报错与解决

### 问题1：报错 "Cannot find module './Hello' or its corresponding type declarations"

**原因：** TypeScript 找不到组件文件或类型声明，常见于 import 路径或扩展名问题。

**解决方法：**
1. 确认 import 路径正确（大小写敏感）
2. 在 tsconfig.json 中确保 `jsx` 设置为 `"react-jsx"`（React 17+）或 `"react"`（旧版）
3. 如果引入第三方库，安装对应的 `@types/` 包：
```bash
npm install --save-dev @types/react @types/react-dom
```
4. 检查 tsconfig.json 的 `baseUrl` 和 `paths` 配置

### 问题2：报错 "Property 'xxx' does not exist on type 'IntrinsicAttributes'"（组件属性不匹配）

**原因：** 给组件传了它 Props 中没有定义的属性，或 Props 类型没写全。

**解决方法：**
```tsx
// 错误：传了 Props 中不存在的属性
<Hello name="小明" color="red" />  // 如果 HelloProps 没有 color，报错

// 方法一：在 Props 中添加该属性
interface HelloProps {
  name: string;
  color?: string;
}

// 方法二：如果确实需要透传所有属性，用扩展运算符
interface HelloProps extends React.HTMLAttributes<HTMLDivElement> {
  name: string;
}
```

### 问题3：报错 "Type 'string' is not assignable to type 'number'"

**原因：** 传给组件的属性类型不对，TypeScript 的类型检查拦住了错误。

**解决方法：**
1. 检查传入值的类型是否与 Props 定义一致
2. 如果是数字，别加引号：用 `age={20}` 而不是 `age="20"`
3. 如果是动态值，确保变量类型正确
4. 如果确实需要联合类型，用 `string | number`

### 问题4：报错 "'React' refers to a UMD global, but the current file is a module"

**原因：** 使用了 JSX 但没有 import React，且 tsconfig.json 配置要求显式导入。

**解决方法：**
```bash
# 方法一：确保 tsconfig.json 中 jsx 设置为 react-jsx（自动导入，推荐）
# "jsx": "react-jsx"

# 方法二：在文件顶部手动导入
import React from 'react';
```

---

## 💡 小知识

- TSX 本质是 TypeScript 对 JSX 语法的支持，TypeScript 编译器内置了 JSX 解析能力
- React 18 + TypeScript 已成为新项目的标配，社区主流组件库（Ant Design、MUI 等）都提供 TS 版本
- 编译后类型信息全部被擦除，打包体积和普通 JS 一样，不影响运行时性能
- `React.FC` 在新版 React 类型中不再自动包含 `children`，如果需要要显式声明

## 🔗 相关链接

- [React 官网](https://react.dev/)
- [TypeScript 官网](https://www.typescriptlang.org/)
- [React + TypeScript 中文教程](https://zh-hans.react.dev/learn/typescript)
- [Vite 官网](https://vitejs.dev/)
- [WebStorm 官网](https://www.jetbrains.com/webstorm/)
