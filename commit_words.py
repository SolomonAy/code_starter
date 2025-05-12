import subprocess
import os
import shutil

# Configuration
SOURCE_FILE = "calculator.py"
DEST_FILE = "my_calc.py"
INDEX_FILE = "word_index.txt"

def check_git_available():
    """Check if Git is installed."""
    return shutil.which("git") is not None

def run_git_command(command):
    """Execute a Git command and handle errors."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Git Error: {e.stderr}")
        exit(1)
    except FileNotFoundError:
        print("Error: Git is not installed or not in PATH.")
        exit(1)

def main():
    # Check if Git is installed
    if not check_git_available():
        print("Error: Git is not installed or not in PATH.")
        exit(1)

    # Ensure we're in a Git repository
    if not os.path.exists(".git"):
        print("Error: Not a Git repository. Please run in a directory with a .git folder.")
        exit(1)

    # Verify source file exists
    if not os.path.exists(SOURCE_FILE):
        print(f"Error: {SOURCE_FILE} not found.")
        exit(1)

    # Read source file and split into words
    with open(SOURCE_FILE, "r") as f:
        content = f.read()
    words = content.split()  # Split on whitespace

    # Get current index (default to 0 if index file doesn't exist)
    current_index = 0
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "r") as f:
            try:
                current_index = int(f.read().strip())
            except ValueError:
                print(f"Error: Invalid content in {INDEX_FILE}.")
                exit(1)

    # Check if there are words left to copy
    if current_index >= len(words):
        print("No more words to copy.")
        return

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
    run_git_command(["git", "commit", "-m", "file updated"])
    print("Changes staged and committed.")

if __name__ == "__main__":
    main()