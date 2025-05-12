# Define file paths
$sourceFile = "calculator.py"
$targetFile = "my_calc.py"
$indexFile = "word_index.txt"

# Check if SOURCE_FILE exists
if (-not (Test-Path $sourceFile)) {
    Write-Error "Source file '$sourceFile' does not exist."
    exit 1
}

# Read all words from SOURCE_FILE (split by whitespace)
$words = Get-Content $sourceFile -Raw | ForEach-Object { $_ -split '\s+' } | Where-Object { $_ }

# Get current index (default to 0 if index file doesn't exist)
if (Test-Path $indexFile) {
    $currentIndex = [int](Get-Content $indexFile)
} else {
    $currentIndex = 0
}

# Check if there are words left to copy
if ($currentIndex -ge $words.Length) {
    Write-Output "No more words to copy."
    exit 0
}

# Copy the current word to TARGET_FILE
$currentWord = $words[$currentIndex]
Set-Content -Path $targetFile -Value $currentWord
Write-Output "Copied word '$currentWord' to $targetFile"

# Increment and save the index
$currentIndex++
Set-Content -Path $indexFile -Value $currentIndex

# Perform Git operations
try {
    git add .
    git commit -m ''
    Write-Output "Changes staged and committed."
} catch {
    Write-Error "Git operation failed: $_"
    exit 1
}