import re
import tkinter as tk
from tkinter import scrolledtext
import sys

# Check if running in a virtual environment
if not hasattr(sys, 'real_prefix') and not sys.base_prefix != sys.prefix:
    print("WARNING: It looks like you're not running this script in a virtual "
          "environment.")
    print("You might encounter errors with dependencies like 'pyperclip'.")
    print("\nTo set up a virtual environment:")
    print("1. Run: bash setup.sh")
    print("2. Activate the environment: source venv/bin/activate")
    print("3. Run this script again: python expenses.py\n")

try:
    import pyperclip  # type: ignore # For clipboard functionality
except ImportError:
    print("ERROR: The 'pyperclip' module is not installed.")
    print("Please run 'bash setup.sh' to set up the virtual environment and "
          "dependencies.")
    sys.exit(1)


def format_amount(amount):
    """Convert decimal points to commas in amount strings."""
    if '.' in amount and ',' not in amount:
        return amount.replace('.', ',')
    return amount


def process_input(input_str):
    # Match different format patterns:
    # 1. Standard format with DD/MM/YYYY HH:MM
    # 2. Format with M/D/YYYY HH:MM AM/PM
    # Process each message block separately
    message_blocks = re.split(r'\n(?=\w+[^,\n]+, \[)', input_str)

    result_str = ""
    for block in message_blocks:
        block = block.strip()
        if not block:
            continue

        # Try different patterns
        # Pattern 1: Name, [DD/MM/YYYY HH:MM]
        # Pattern 2: Name, [M/D/YYYY HH:MM AM/PM]
        patterns = [
            (r'(?:.+), \[(?:\d{1,2}/\d{1,2}/\d{4} '
             r'\d{1,2}:\d{1,2}(?:\s?[AP]M)?)\]\s*\n([\d,\.]+)\s+(.+)'),
            (r'(?:.+), \[(?:\d{1,2}/\d{1,2}/\d{4} '
             r'\d{1,2}:\d{1,2}(?:\s?[AP]M)?)\]\s*\n([\d,\.]+)\s+(.+)')
        ]

        matched = False
        for pattern in patterns:
            match = re.search(pattern, block)
            if match:
                amount = format_amount(match.group(1).strip())
                description = match.group(2).strip()
                result_str += f"{description}\t€ {amount}\n"
                matched = True
                break

        # If no match was found, try a more relaxed pattern
        if not matched and re.search(r'\d+[,\.]?\d*', block):
            # Look for amount and description in the text
            # following the timestamp
            after_timestamp = re.split(r'\]\s*\n', block)
            if len(after_timestamp) > 1:
                content = after_timestamp[1].strip()
                # Extract amount and description
                amount_match = re.match(r'([\d,\.]+)\s+(.+)', content)
                if amount_match:
                    amount = format_amount(amount_match.group(1).strip())
                    description = amount_match.group(2).strip()
                    result_str += f"{description}\t€ {amount}\n"

    return result_str.strip()


def create_gui():
    # Create main window
    root = tk.Tk()
    root.title("Telegram Expenses Parser")
    root.geometry("800x600")

    # Create frame for instructions
    instruction_frame = tk.Frame(root)
    instruction_frame.pack(fill=tk.X, padx=10, pady=5)

    # Add instructions label
    instructions = """Copy your telegram messages here"""

    instruction_label = tk.Label(instruction_frame,
                                 text=instructions,
                                 justify=tk.LEFT,
                                 anchor="w")
    instruction_label.pack(fill=tk.X)

    # Create frame for text areas
    text_frame = tk.Frame(root)
    text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    # Configure columns to be equal width
    text_frame.columnconfigure(0, weight=1)
    text_frame.columnconfigure(1, weight=1)

    # Input area
    input_label = tk.Label(text_frame, text="Input (Paste Telegram text):")
    input_label.grid(row=0, column=0, sticky=tk.W)

    input_text = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD)
    input_text.grid(row=1, column=0, sticky=tk.NSEW, padx=(0, 5))

    # Output area
    output_label = tk.Label(text_frame, text="Output (Formatted text):")
    output_label.grid(row=0, column=1, sticky=tk.W)

    output_text = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD)
    output_text.grid(row=1, column=1, sticky=tk.NSEW, padx=(5, 0))

    # Configure the row to expand
    text_frame.rowconfigure(1, weight=1)

    # Create frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.X, padx=10, pady=10)

    # Function to process input
    def on_process():
        input_content = input_text.get("1.0", tk.END)
        output_content = process_input(input_content)
        output_text.delete("1.0", tk.END)
        output_text.insert("1.0", output_content)

    # Function to copy output to clipboard
    def on_copy():
        output_content = output_text.get("1.0", tk.END).strip()
        pyperclip.copy(output_content)

    # Function to clear input
    def on_clear_input():
        input_text.delete("1.0", tk.END)

    # Function to clear output
    def on_clear_output():
        output_text.delete("1.0", tk.END)

    # Add buttons
    process_button = tk.Button(button_frame,
                               text="Process",
                               command=on_process)
    process_button.pack(side=tk.LEFT, padx=5)

    copy_button = tk.Button(button_frame,
                            text="Copy Output",
                            command=on_copy)
    copy_button.pack(side=tk.LEFT, padx=5)

    clear_input_button = tk.Button(button_frame,
                                   text="Clear Input",
                                   command=on_clear_input)
    clear_input_button.pack(side=tk.LEFT, padx=5)

    clear_output_button = tk.Button(button_frame,
                                    text="Clear Output",
                                    command=on_clear_output)
    clear_output_button.pack(side=tk.LEFT, padx=5)

    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    create_gui()
