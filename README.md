# 🛒 Shopee Link Converter

เครื่องมือแปลงลิงค์ Shopee ให้เป็นรูปแบบสั้นและใช้งานง่าย

## ✨ คุณสมบัติ

- 🔗 แปลงลิงค์ Shopee เป็นรูปแบบสั้น
- 🌐 Web Application (Flask)
- 💻 Desktop Application (.exe)
- 📱 Responsive Design
- ⚡ ใช้งานง่าย รวดเร็ว

## 🚀 การใช้งาน

### Web Application
1. เข้าไปที่ [Live Demo](https://your-app-name.herokuapp.com)
2. วางลิงค์ Shopee ที่ต้องการแปลง
3. กด "แปลงลิงค์"
4. คัดลอกลิงค์สั้นที่ได้

### Desktop Application
1. ดาวน์โหลด `ShopeeLinkConverter.exe`
2. Double-click เพื่อเปิดโปรแกรม
3. ใช้งานเหมือน Web Application

## 🛠️ การติดตั้ง

### สำหรับ Developer

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/shopee-new.git
cd shopee-new

# ติดตั้ง dependencies
pip install -r requirements.txt

# รัน Web Application
python app.py

# รัน Desktop Application
python main.py
```

### Build Desktop Application

```bash
# ใช้ build script
python build_script.py

# หรือใช้ PyInstaller โดยตรง
pyinstaller ShopeeLinkConverter.spec
```

## 📦 Dependencies

- Flask==2.3.3
- pywebview==4.4.1
- pyinstaller==6.3.0

## 🏗️ โครงสร้างโปรเจค

```
shopee-new/
├── app.py                          # Flask application
├── main.py                         # Desktop app entry point
├── requirements.txt                # Dependencies
├── build_script.py                 # Build automation
├── ShopeeLinkConverter.spec        # PyInstaller spec
├── templates/                      # HTML templates
│   └── index.html
└── README.md                       # This file
```

## 🔧 การ Deploy

### Web Application
- **Heroku**: ง่ายที่สุด ฟรี tier
- **Railway**: ฟรี 500 hours/เดือน
- **Render**: ฟรี tier พร้อม SSL

### Desktop Application
- **Windows**: ใช้ PyInstaller หรือ auto-py-to-exe
- **Mac**: ใช้ PyInstaller สร้าง .app
- **Linux**: ใช้ PyInstaller สร้าง binary

## 📋 รูปแบบลิงค์ที่รองรับ

- `.i.SHOP_ID.PRODUCT_ID`
- `-i.SHOP_ID.PRODUCT_ID`
- `/product/SHOP_ID/PRODUCT_ID`

## 🤝 การมีส่วนร่วม

1. Fork repository
2. สร้าง feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. เปิด Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 ขอบคุณ

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [PyWebView](https://pywebview.flowrl.com/) - Desktop GUI
- [PyInstaller](https://pyinstaller.org/) - Executable builder

---

**Made with ❤️ by [Your Name]**
