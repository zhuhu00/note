# NeoVim

参考这个人的进行配置

https://github.com/cxzhou35/Awesome-neovim/tree/lazy

- 字体上选择了https://www.programmingfonts.org/#lilex

- 安装 C++ 和 Python 的 LSP 服务器，你需要安装适用于这两种语言的 LSP 插件。通常来说，对于 C++，你可以使用 `clangd` 作为 LSP 服务器，而对于 Python，你可以使用 `pylsp`。在 Neovim 中安装这两个服务器的方法如下：

1. **安装 clangd**：
   
   ```
   :LspInstall clangd
   ```

   这将安装 C++ 的 LSP 服务器 clangd。

2. **安装 pylsp**：

   ```
   :LspInstall pylsp
   ```

   这将安装 Python 的 LSP 服务器 pylsp。

