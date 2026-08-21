#!/usr/bin/env bash

set -e

echo
echo "=============================="
echo "       WPForge Release"
echo "=============================="
echo

if [ -z "$1" ]; then
    echo "Usage:"
    echo "  ./release.sh 1.0.0"
    echo
    echo "Example:"
    echo "  ./release.sh 1.2.0"
    exit 1
fi

VERSION="$1"
TAG="v${VERSION}"

echo "Version: $VERSION"
echo "Tag:     $TAG"
echo

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "[ERROR] This directory is not a Git repository."
    exit 1
fi

if ! git diff --quiet; then
    echo "[ERROR] You have uncommitted changes."
    echo "Commit or stash them before creating a release."
    exit 1
fi

if ! git diff --cached --quiet; then
    echo "[ERROR] You have staged changes that are not committed."
    exit 1
fi

if ! git remote get-url origin >/dev/null 2>&1; then
    echo "[ERROR] Git remote 'origin' was not found."
    exit 1
fi

if git rev-parse "$TAG" >/dev/null 2>&1; then
    echo "[ERROR] Tag $TAG already exists."
    exit 1
fi

echo "Pulling latest changes..."
git pull --rebase origin main

echo
echo "Creating release commit..."

git commit --allow-empty -m "Release $TAG"

echo
echo "Creating tag $TAG..."

git tag -a "$TAG" -m "Release $TAG"

echo
echo "Pushing commit..."

git push origin main

echo
echo "Pushing tag..."

git push origin "$TAG"

echo
echo "=============================="
echo "Release $TAG created!"
echo "=============================="
echo
echo "GitHub Actions should now build and publish the release."
echo
