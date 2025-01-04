# English Version

## Remember Me

This program allows you to learn, test, and manage vocabulary lists. It also provides optional AI-powered validation and example-sentence generation features through Kimi AI (example link).

### 1. Prerequisites and Installation

1. **Install Python 3.**  
2. **Install the package** (example command if you have built and published it):
   ```bash
   pip install remember_me_gre
   ```
3. Prepare a CSV file with vocabulary words (e.g., word_sheets/Word_Sheet1.csv).

### 2. Enabling AI Features (MOONSHOT_API_KEY)
To use AI validation and example-sentence generation, you need an API key from Kimi AI. Follow these steps:

1. Sign up / log in to Kimi AI and create a new API key.
2. Set an environment variable MOONSHOT_API_KEY. Below are two simple methods:


#### Method A (macOS / Linux)
1.	Open a terminal.
2.	Append the following to your ~/.bashrc or ~/.zshrc:
    ```bash
    export MOONSHOT_API_KEY="YOUR_KIMI_AI_KEY"
    ```
3. Run source ~/.bashrc (or source ~/.zshrc) to apply changes.

#### Method B (Windows)
1. Open Command Prompt or PowerShell.
2. Type:
    ```bash
    set MOONSHOT_API_KEY=YOUR_KIMI_AI_KEY
    ```

3. press enter

Tip: You can also permanently set it in “System Properties → Environment Variables” by creating a new user variable named MOONSHOT_API_KEY with your API key.

### 3. Usage
1. Run the program:
    ```bash
    remember_me
    ```


2. Specify the path to your vocabulary file when prompted (e.g., word_sheets/Word_Sheet1.csv).

3. Follow the on-screen menu to choose a mode:
- Learning Mode: View definitions in order or randomly.
- Testing Mode: Enter the meaning yourself and get real-time validation.
- Section Testing/Learning: Focus on specific sections if your CSV is divided by “Section 1”, “Section 2”, etc.
- Manage Starred Words: Add, remove, or test specifically starred words.

If you have set MOONSHOT_API_KEY, the program will attempt AI-based validation whenever the local method fails. It can also generate example sentences with translations.

