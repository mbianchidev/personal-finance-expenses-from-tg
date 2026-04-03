@echo off
echo Setting up Telegram Expenses Parser environment...

if not exist win-venv (
    echo Creating virtual environment...
    python -m venv win-venv
    if errorlevel 1 (
        echo Failed to create virtual environment. Please make sure Python is installed correctly.
        exit /b 1
    )
    echo Virtual environment created successfully!
) else (
    echo Virtual environment already exists.
)

echo Activating virtual environment...
call .\win-venv\Scripts\activate.bat

echo Checking dependencies...
python -c "import pyperclip" 2>nul
if errorlevel 1 (
    echo Installing required dependencies...
    pip install --quiet pyperclip
    if errorlevel 1 (
        echo Failed to install dependencies.
        exit /b 1
    )
) else (
    echo All dependencies already installed.
)

call .\win-venv\Scripts\activate.bat
echo Running the application...
python expenses.py