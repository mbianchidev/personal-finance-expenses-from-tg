# Colors for better output
function Write-ColorOutput($ForegroundColor) {
  $fc = $host.UI.RawUI.ForegroundColor
  $host.UI.RawUI.ForegroundColor = $ForegroundColor
  if ($args) {
      Write-Output $args
  }
  $host.UI.RawUI.ForegroundColor = $fc
}

Write-ColorOutput Yellow "Setting up Telegram Expenses Parser environment..."

# Create virtual environment if it doesn't exist
if (-not (Test-Path -Path "win-venv")) {
  Write-ColorOutput Yellow "Creating virtual environment..."
  try {
      python -m venv win-venv
      Write-ColorOutput Green "Virtual environment created successfully!"
  }
  catch {
      Write-Output "Failed to create virtual environment. Please make sure Python is installed correctly."
      exit 1
  }
}
else {
  Write-ColorOutput Green "Virtual environment already exists."
}

# Activate virtual environment
Write-ColorOutput Yellow "Activating virtual environment..."
& .\win-venv\Scripts\Activate.ps1

# Install dependencies
Write-ColorOutput Yellow "Installing required dependencies..."
try {
  pip install pyperclip
  Write-ColorOutput Green "Dependencies installed successfully!"
}
catch {
  Write-Output "Failed to install dependencies."
  exit 1
}

Write-ColorOutput Green "Setup completed successfully!"
Write-ColorOutput Yellow "To run the application:"
Write-ColorOutput Yellow "  1. " -NoNewline
Write-ColorOutput Green ".\win-venv\Scripts\Activate.ps1" -NoNewline
Write-ColorOutput Yellow " (if not already activated)"
Write-ColorOutput Yellow "  2. " -NoNewline
Write-ColorOutput Green "python expenses.py"
Write-ColorOutput Yellow "Enjoy!"