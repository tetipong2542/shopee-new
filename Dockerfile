# Use Windows-based Python image for cross-compilation
FROM python:3.9-windowsservercore

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application files
COPY . .

# Build executable
RUN pyinstaller --onefile --windowed --name=ShopeeLinkConverter --add-data=templates;templates main.py

# The executable will be in dist/ShopeeLinkConverter.exe
