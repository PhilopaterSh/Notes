# Get the current date and format it for the commit message
$commitMessage = Get-Date -Format "yyyy-MM-dd"

# Explain the 'git add' command
Write-Host "Staging all changes in the current directory..."
git add .

# Explain the 'git commit' command
Write-Host "Committing changes with the message: $commitMessage"
git commit -m "$commitMessage"

# Explain the 'git push' command
Write-Host "Pushing changes to the remote repository..."
git push

Write-Host "Deployment script finished."
