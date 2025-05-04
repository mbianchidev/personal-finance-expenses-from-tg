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

echo Installing required dependencies...
pip install pyperclip
if errorlevel 1 (
    echo Failed to install dependencies.
    exit /b 1
)

call .\win-venv\Scripts\activate.bat
echo Running the application...
python expenses.py

echo.
echo Setup completed successfully!
echo.
echo To run the application:
echo   1. call .\win-venv\Scripts\activate.bat (if not already activated)
echo   2. python expenses.py
echo.
echo Enjoy!