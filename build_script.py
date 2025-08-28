#!/usr/bin/env python3
"""
Build script for Shopee Link Converter Desktop App
"""
import os
import sys
import subprocess
import shutil

def install_dependencies():
    """Install required dependencies"""
    print("Installing dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def build_exe():
    """Build the executable using PyInstaller"""
    print("Building executable...")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",                    # Single executable file
        "--windowed",                   # No console window
        "--name=ShopeeLinkConverter",   # Executable name
        "--add-data=templates:templates",  # Include templates folder
        "--icon=icon.ico",              # Icon (if available)
        "--clean",                      # Clean cache
        "main.py"
    ]
    
    # Remove icon option if icon doesn't exist
    if not os.path.exists("icon.ico"):
        cmd.remove("--icon=icon.ico")
    
    subprocess.run(cmd)

def create_distribution():
    """Create distribution folder with executable"""
    print("Creating distribution...")
    
    # Create dist folder if it doesn't exist
    if not os.path.exists("dist"):
        os.makedirs("dist")
    
    # Copy executable to dist folder
    if os.path.exists("dist/ShopeeLinkConverter.exe"):
        print("Executable created successfully!")
        print("Location: dist/ShopeeLinkConverter.exe")
    else:
        print("Error: Executable not found!")

def main():
    """Main build process"""
    print("=== Shopee Link Converter Build Process ===")
    
    # Step 1: Install dependencies
    install_dependencies()
    
    # Step 2: Build executable
    build_exe()
    
    # Step 3: Create distribution
    create_distribution()
    
    print("=== Build Complete ===")

if __name__ == "__main__":
    main()
