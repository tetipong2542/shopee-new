# Cross-Compilation Guide (Advanced)

## วิธีที่ 4: ใช้ Cross-Compilation Tools

### ข้อควรระวัง:
- ซับซ้อนและไม่เสถียร
- อาจมีปัญหา compatibility
- ต้องใช้เครื่องมือพิเศษ

### ขั้นตอนที่ 1: ติดตั้ง Wine
```bash
# บน Mac
brew install wine

# หรือใช้ CrossOver (GUI version)
```

### ขั้นตอนที่ 2: ติดตั้ง Python บน Wine
```bash
# ดาวน์โหลด Python Windows installer
wine python-3.9.x-amd64.exe

# ติดตั้ง pip
wine python -m ensurepip
```

### ขั้นตอนที่ 3: Build ผ่าน Wine
```bash
# ติดตั้ง dependencies
wine pip install -r requirements.txt

# Build executable
wine pyinstaller --onefile --windowed main.py
```

### ข้อจำกัด:
- ไม่เสถียร
- อาจมีปัญหา dependencies
- ไฟล์ขนาดใหญ่
- ไม่แนะนำสำหรับ production
