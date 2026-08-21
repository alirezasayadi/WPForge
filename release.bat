@echo off
setlocal

title WPForge Release

echo.
echo ==============================
echo        WPForge Release
echo ==============================
echo.

if "%~1"=="" (
    echo Usage:
    echo   release.bat 1.0.0
    echo.
    echo Example:
    echo   release.bat 1.2.0
    exit /b 1
)

set "VERSION=%~1"
set "TAG=v%VERSION%"

echo Version: %VERSION%
echo Tag:     %TAG%
echo.

git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo [ERROR] This directory is not a Git repository.
    exit /b 1
)

git diff --quiet
if errorlevel 1 (
    echo [ERROR] You have uncommitted changes.
    echo Commit or stash them before creating a release.
    exit /b 1
)

git diff --cached --quiet
if errorlevel 1 (
    echo [ERROR] You have staged changes that are not committed.
    exit /b 1
)

git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git remote 'origin' was not found.
    exit /b 1
)

git rev-parse "%TAG%" >nul 2>&1
if not errorlevel 1 (
    echo [ERROR] Tag %TAG% already exists.
    exit /b 1
)

echo Pulling latest changes...
git pull --rebase origin main
if errorlevel 1 (
    echo [ERROR] Failed to update from origin.
    exit /b 1
)

echo.
echo Creating release commit...

git commit --allow-empty -m "Release %TAG%"
if errorlevel 1 (
    echo [ERROR] Failed to create release commit.
    exit /b 1
)

echo.
echo Creating tag %TAG%...

git tag -a "%TAG%" -m "Release %TAG%"
if errorlevel 1 (
    echo [ERROR] Failed to create Git tag.
    exit /b 1
)

echo.
echo Pushing commit...

git push origin main
if errorlevel 1 (
    echo [ERROR] Failed to push main branch.
    exit /b 1
)

echo.
echo Pushing tag...

git push origin "%TAG%"
if errorlevel 1 (
    echo [ERROR] Failed to push tag.
    exit /b 1
)

echo.
echo ==============================
echo Release %TAG% created!
echo ==============================
echo.
echo GitHub Actions should now build and publish the release.
echo.

endlocal
