import subprocess
import os

# Configuration Variables
SOURCE_FILE = "calculator.py"
DEST_FILE = "my_calc.py"
INDEX_FILE = "word_index.txt"

def run_git_command(args):
    """Execute a Git command and handle errors."""
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Git Error: {e.stderr} (Command: {' '.join(args)})")
        exit(1)
    except FileNotFoundError:
        print("Error: Git is not installed or not in PATH.")
        exit(1)

def main():
    # Verify source file exists
    if not os.path.exists(SOURCE_FILE):
        print(f"Error: {SOURCE_FILE} not found.")
        exit(1)

    # Read all words from source file (split by whitespace)
    with open(SOURCE_FILE, "r") as f:
        words = f.read().split()

    # Get current index (default to 0 if index file doesn't exist)
    current_index = 0
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "r") as f:
            try:
                current_index = int(f.read().strip())
            except ValueError:
                print(f"Error: Invalid index in {INDEX_FILE}.")
                exit(1)

    # Check if there are words left to copy
    if current_index >= len(words):
        print("No more words to copy.")
        exit(0)

    # Copy the current word to DEST_FILE
    current_word = words[current_index]
    with open(DEST_FILE, "w") as f:
        f.write(current_word)
    print(f"Copied word '{current_word}' to {DEST_FILE}")

    # Increment and save the index
    with open(INDEX_FILE, "w") as f:
        f.write(str(current_index + 1))

    # Perform Git operations
    run_git_command(["git", "add", "."])
    run_git_command(["git", "commit", "-m", "", "--allow-empty-message"])
    print("Changes staged and committed.")

if __name__ == "__main__":
    main()