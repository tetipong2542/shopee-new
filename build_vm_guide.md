# Build .exe ผ่าน Virtual Machine

## วิธีที่ 3: ใช้ Windows Virtual Machine

### ขั้นตอนที่ 1: ติดตั้ง Virtual Machine
1. **Parallels Desktop** (แนะนำสำหรับ Mac)
2. **VMware Fusion**
3. **VirtualBox** (ฟรี)

### ขั้นตอนที่ 2: ติดตั้ง Windows
1. ดาวน์โหลด Windows 10/11 ISO
2. ติดตั้งใน VM
3. ติดตั้ง Python 3.9+

### ขั้นตอนที่ 3: Build .exe
```bash
# ใน Windows VM
git clone <your-repo>
cd shopee-new
pip install -r requirements.txt
pyinstaller --onefile --windowed --name=ShopeeLinkConverter --add-data="templates;templates" main.py
```

### ขั้นตอนที่ 4: Copy ไฟล์
- Copy `dist/ShopeeLinkConverter.exe` ออกจาก VM
- ไฟล์พร้อมใช้งานบน Windows จริง
