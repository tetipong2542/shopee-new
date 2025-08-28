@echo off
echo ========================================
echo Shopee Link Converter - Build Script
echo ========================================
echo.

echo Step 1: Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Step 2: Building executable...
pyinstaller ShopeeLinkConverter.spec
if %errorlevel% neq 0 (
    echo Error: Failed to build executable
    pause
    exit /b 1
)

echo.
echo Step 3: Checking output...
if exist "dist\ShopeeLinkConverter.exe" (
    echo Success! Executable created at: dist\ShopeeLinkConverter.exe
    echo File size:
    dir "dist\ShopeeLinkConverter.exe" | find "ShopeeLinkConverter.exe"
) else (
    echo Error: Executable not found!
)

echo.
echo ========================================
echo Build process completed!
echo ========================================
pause
