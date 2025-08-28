# Shopee Link Converter - Desktop Application

## คำแนะนำการ Build Desktop Application

### ข้อกำหนดเบื้องต้น

1. **Python 3.8+** ติดตั้งแล้ว
2. **Windows OS** (สำหรับ build .exe)
3. **Internet connection** สำหรับดาวน์โหลด dependencies

### ขั้นตอนการ Build

#### วิธีที่ 1: ใช้ Build Script (แนะนำ)

```bash
# 1. ติดตั้ง dependencies
pip install -r requirements.txt

# 2. รัน build script
python build_script.py
```

#### วิธีที่ 2: ใช้ PyInstaller โดยตรง

```bash
# 1. ติดตั้ง dependencies
pip install -r requirements.txt

# 2. Build executable
pyinstaller --onefile --windowed --name=ShopeeLinkConverter --add-data=templates:templates main.py
```

#### วิธีที่ 3: ใช้ auto-py-to-exe (GUI)

```bash
# 1. ติดตั้ง auto-py-to-exe
pip install auto-py-to-exe

# 2. รัน GUI
auto-py-to-exe

# 3. ตั้งค่าใน GUI:
#    - Script Location: main.py
#    - Onefile: ✓
#    - Window Based: ✓
#    - Additional Files: templates/
```

### การตั้งค่าใน auto-py-to-exe

1. **Script Location**: เลือกไฟล์ `main.py`
2. **Onefile**: ✓ (สร้างไฟล์เดียว)
3. **Window Based**: ✓ (ไม่มี console window)
4. **Additional Files**: เพิ่ม `templates/` folder
5. **Output Directory**: เลือกโฟลเดอร์ที่ต้องการ
6. **Icon**: เพิ่ม icon.ico (ถ้ามี)

### โครงสร้างไฟล์ที่จำเป็น

```
shopee-new/
├── app.py                 # Flask application
├── main.py               # Desktop app entry point
├── requirements.txt      # Dependencies
├── build_script.py      # Build automation
├── templates/           # HTML templates
│   └── index.html
└── README_DESKTOP.md    # This file
```

### การทดสอบ

1. **ทดสอบบน Mac/Linux**:
   ```bash
   python main.py
   ```

2. **ทดสอบบน Windows**:
   ```bash
   python main.py
   ```

3. **ทดสอบ .exe**:
   - Double-click ไฟล์ `ShopeeLinkConverter.exe`
   - หรือรันจาก command line

### การแก้ไขปัญหา

#### ปัญหา: Import Error
```bash
# ตรวจสอบ dependencies
pip list | grep -E "(Flask|pywebview|pyinstaller)"
```

#### ปัญหา: Templates not found
```bash
# ตรวจสอบว่า templates folder อยู่ในตำแหน่งที่ถูกต้อง
ls -la templates/
```

#### ปัญหา: Port already in use
```python
# แก้ไขใน main.py - เปลี่ยน port
app.run(host='127.0.0.1', port=5001, debug=False)
```

### การแจกจ่าย

1. **ไฟล์เดียว**: `ShopeeLinkConverter.exe`
2. **ขนาดไฟล์**: ประมาณ 50-100 MB
3. **ความต้องการ**: Windows 7+ (64-bit)

### หมายเหตุสำคัญ

- **Antivirus**: บาง antivirus อาจ detect เป็น false positive
- **File size**: ไฟล์จะมีขนาดใหญ่เพราะรวม Python runtime
- **Performance**: การเริ่มต้นอาจช้าเล็กน้อย
- **Updates**: ต้อง build ใหม่เมื่อมีการอัปเดต

### การปรับแต่งเพิ่มเติม

#### เพิ่ม Icon
1. สร้างไฟล์ `icon.ico`
2. เพิ่มใน PyInstaller command: `--icon=icon.ico`

#### ปรับขนาด Window
แก้ไขใน `main.py`:
```python
webview.create_window(
    'Shopee Link Converter', 
    'http://127.0.0.1:5000',
    width=1200,    # ปรับความกว้าง
    height=800,    # ปรับความสูง
    resizable=True
)
```

#### เพิ่ม Splash Screen
```python
# เพิ่มใน main.py
webview.create_window(
    'Shopee Link Converter', 
    'http://127.0.0.1:5000',
    width=1000,
    height=700,
    resizable=True,
    text_select=True,
    # เพิ่ม splash screen
    splash_screen=True
)
```
