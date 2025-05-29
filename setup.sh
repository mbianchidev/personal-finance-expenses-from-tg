#!/bin/zsh

# Colors for better output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Setting up Telegram Expenses Parser environment...${NC}"

# First, delete existing virtual environment if it exists
if [ -d "venv" ]; then
    echo -e "${YELLOW}Removing existing virtual environment...${NC}"
    rm -rf venv
    echo -e "${GREEN}Removed old virtual environment.${NC}"
fi

# Create new virtual environment
echo -e "${YELLOW}Creating fresh virtual environment...${NC}"
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Failed to create virtual environment. Please make sure python3-venv is installed."
    exit 1
fi
echo -e "${GREEN}Virtual environment created successfully!${NC}"

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

# Verify Python path is correct
echo -e "${YELLOW}Checking Python path...${NC}"
echo "Python interpreter: $(which python)"

# Install dependencies using the properly activated environment's pip
echo -e "${YELLOW}Installing required dependencies...${NC}"
python -m pip install --upgrade pip
python -m pip install pyperclip
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies."
    exit 1
fi

echo -e "${GREEN}Setup completed successfully!${NC}"
echo -e "${YELLOW}To run the application:${NC}"
echo -e "  1. ${GREEN}source venv/bin/activate${NC} (if not already activated)"
echo -e "  2. ${GREEN}python expenses.py${NC}"
echo -e "${YELLOW}Enjoy!${NC}"

source venv/bin/activate
python expenses-macbook.py