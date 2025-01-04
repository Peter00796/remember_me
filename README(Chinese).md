# 中文版

## 记住我

这个程序允许您学习、测试和管理词汇表。它还通过 Kimi AI 提供可选的 AI 驱动验证和例句生成功能（示例链接）。

### 1. 先决条件和安装

1. **安装 Python 3。**  
2. **安装软件包**
    ```bash
    pip install remember-me
    ```
3. 准备一个包含词汇的 CSV 文件（例如，word_sheets/Word_Sheet1.csv）。

### 2. 启用 AI 功能（MOONSHOT_API_KEY）
要使用 AI 验证和例句生成功能，您需要从 Kimi AI 获取 API 密钥。请按照以下步骤操作：

1. 注册 / 登录 Kimi AI 并创建一个新的 API 密钥。
2. 设置环境变量 MOONSHOT_API_KEY。以下是两种简单的方法：

#### 方法 A（macOS / Linux）
1. 打开终端。
2. 将以下内容添加到您的 ~/.bashrc 或 ~/.zshrc 中：
     ```bash
     export MOONSHOT_API_KEY="YOUR_KIMI_AI_KEY"
     ```
3. 运行 source ~/.bashrc（或 source ~/.zshrc）以应用更改。

#### 方法 B（Windows）
1. 打开命令提示符或 PowerShell。
2. 输入：
     ```bash
     set MOONSHOT_API_KEY=YOUR_KIMI_AI_KEY
     ```
3. 按回车键。

提示：您还可以在“系统属性 → 环境变量”中永久设置它，方法是创建一个名为 MOONSHOT_API_KEY 的新用户变量，并将您的 API 密钥作为值。

### 3. 使用方法
1. 运行程序：
     ```bash
     remember_me
     ```

2. 在提示时指定词汇文件的路径（例如，word_sheets/Word_Sheet1.csv）。

3. 按照屏幕上的菜单选择模式：
- 学习模式：按顺序或随机查看定义。
- 测试模式：自己输入含义并获得实时验证。
- 部分测试/学习：如果您的 CSV 按“Section 1”、“Section 2”等划分，可以专注于特定部分。
- 管理加星词汇：添加、删除或专门测试加星词汇。

如果您设置了 MOONSHOT_API_KEY，程序将在本地方法失败时尝试 AI 驱动的验证。它还可以生成带有翻译的例句。
