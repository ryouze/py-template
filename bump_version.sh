#!/bin/bash
#
# bump_version.sh
#
# Updates the version in pyproject.toml, commits the change, creates a Git tag, and optionally pushes both to the remote repository.
#
# Usage:
#   ./bump_version.sh
#
# Prompts for the new version after displaying the current one.
# Assumes the main Git branch is named 'main' and that pyproject.toml contains a top-level 'version = "x.y.z"' line.

set -e

# Extract current version
current_version=$(grep -E '^version = "' pyproject.toml | head -n1 | cut -d'"' -f2)
if [[ -z "$current_version" ]]; then
    echo "Error: Could not find version in pyproject.toml"
    exit 1
fi

echo "Current version: $current_version"
read -rp "Enter new version (e.g. 1.2.3): " new_version

# Validate version format
if [[ ! "$new_version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "Invalid version format. Expected format: X.Y.Z"
    exit 1
fi

# Detect platform and set sed command accordingly
if [[ "$OSTYPE" == "darwin"* ]]; then
    sed -i '' "s/^version = \".*\"/version = \"$new_version\"/" pyproject.toml
else
    sed -i "s/^version = \".*\"/version = \"$new_version\"/" pyproject.toml
fi

# Commit the change
git add pyproject.toml
git commit -m "Bumped version to $new_version."

# Create Git tag
git tag "v$new_version"

# Ask to push
read -rp "Push commit and tag to origin? [y/N]: " confirm
if [[ "$confirm" =~ ^[Yy]$ ]]; then
    git push origin main
    git push origin "v$new_version"
else
    echo "Skipped push."
fi
