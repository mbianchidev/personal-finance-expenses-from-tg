# personal-finance-expenses-from-tg
A simple GUI in Python to extract financial expenses from Telegram messages and create entries in a Google Spreadsheet

## Linux / MacOS

Example of how to run the application on Linux or MacOS.

```
just run setup.sh
```

## Windows

Run these commands in the Windows command line (cmd) or PowerShell from the repo folder.

```bash

# Create a new virtual environment (if not already created)
python -m venv win-venv

# Activate the virtual environment
.\win-venv\Scripts\activate

# Install dependencies
pip install pyperclip

# Run the application
python expenses.py
```

Or run the .bat/ps1 files.