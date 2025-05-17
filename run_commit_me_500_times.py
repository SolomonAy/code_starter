import subprocess
import sys
import os

# Configuration
SCRIPT_TO_RUN = "commit_words.py"
RUN_COUNT = 500

def run_script(script_path):
    """Run a Python script and return its output and exit code."""
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            check=False
        )
        return result.stdout, result.stderr, result.returncode
    except FileNotFoundError:
        return "", f"Error: {script_path} not found.", 1
    except subprocess.SubprocessError as e:
        return "", f"Error running {script_path}: {str(e)}", 1

def main():
    # Verify script exists
    if not os.path.exists(SCRIPT_TO_RUN):
        print(f"Error: {SCRIPT_TO_RUN} not found in current directory.")
        sys.exit(1)

    # Run the script 500 times
    for i in range(1, RUN_COUNT + 1):
        print(f"Run {i}/{RUN_COUNT}: Executing {SCRIPT_TO_RUN}...")
        stdout, stderr, exit_code = run_script(SCRIPT_TO_RUN)

        # Print output
        if stdout:
            print(stdout.strip())
        if stderr:
            print(stderr.strip())

        # Check exit code
        if exit_code != 0:
            print(f"Run {i} failed with exit code {exit_code}. Stopping.")
            sys.exit(1)

        # Check for completion (e.g., "No more words to copy")
        if "No more words to copy" in stdout:
            print(f"Completed all words after {i} runs.")
            break

    print(f"Finished executing {SCRIPT_TO_RUN} {i} times.")

if __name__ == "__main__":
    main()