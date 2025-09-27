# PhalanxScreen - Educational Ransomware Simulation

![License](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge&logo=gnu)
![Platform](https://img.shields.io/badge/Platform-Android-green?style=for-the-badge&logo=android)
![Language](https://img.shields.io/badge/Language-Java-orange?style=for-the-badge&logo=java)
![Build](https://img.shields.io/badge/Build-Sketchware-purple?style=for-the-badge&logo=androidstudio)
![Termux](https://img.shields.io/badge/Termux-Linux-black?style=for-the-badge&logo=termux)


![GitHub stars](https://img.shields.io/github/stars/REYHAN6610/PhalanxLocks?style=social)
![GitHub forks](https://img.shields.io/github/forks/REYHAN6610/PhalanxLocks?style=social)
![GitHub issues](https://img.shields.io/github/issues/REYHAN6610/PhalanxLocks)
![GitHub last commit](https://img.shields.io/github/last-commit/REYHAN6610/PhalanxLocks)

---

## 🎯 Pembukaan

Selamat datang di **PhalanxScreen Educational Tool** - sebuah proyek edukasi yang dirancang untuk memahami cara kerja ransomware tipe screen locker pada platform Android. Tool ini menggunakan permission `SYSTEM_ALERT_WINDOW` untuk mendemonstrasikan bagaimana malware dapat mengambil alih layar perangkat Android.

### Mengapa Tool Ini Dibuat?

- 📚 **Edukasi Keamanan Siber**: Membantu peneliti dan mahasiswa memahami cara kerja ransomware
- 🔍 **Analisis Malware**: Menyediakan contoh nyata untuk analisis behavior malware
- 🛡️ **Awareness**: Meningkatkan kesadaran tentang ancaman ransomware di Android
- 🧪 **Research**: Mendukung penelitian dalam bidang mobile security

---

## 🦠 Apa itu PhalanxScreen?

**PhalanxScreen** adalah simulasi ransomware tipe **Screen Locker** yang memanfaatkan permission `SYSTEM_ALERT_WINDOW` untuk mengunci layar perangkat Android. Berbeda dengan ransomware enkripsi yang mengenkripsi file, screen locker hanya memblokir akses ke interface pengguna.

### Karakteristik PhalanxScreen:

| Fitur | Deskripsi |
|-------|-----------|
| **Tipe** | Screen Locker Ransomware |
| **Target** | Android < 8.0 (API Level < 26) |
| **Permission** | SYSTEM_ALERT_WINDOW |
| **Metode** | Overlay Window Attack |
| **Persistensi** | Service Background |

### Mengapa Efektif di Android < 8?

🔹 **Permission Model Lama**: Android versi lama memiliki kontrol permission yang lebih lemah  
🔹 **SYSTEM_ALERT_WINDOW**: Permission ini memberikan akses luas untuk membuat overlay  
🔹 **Background Service**: Layanan dapat berjalan tanpa batasan ketat  
🔹 **User Awareness**: Pengguna Android lama kurang aware terhadap permission berbahaya

---

## ⚙️ Cara Kerja Ransomware

### Alur Kerja PhalanxScreen:

```mermaid
graph TD
    A[App Installation] --> B[Request SYSTEM_ALERT_WINDOW]
    B --> C[Permission Granted]
    C --> D[Start Background Service]
    D --> E[Create Fullscreen Overlay]
    E --> F[Block User Interaction]
    F --> G[Display Ransom Message]
    G --> H[Wait for Payment/Unlock]
```

### Teknis Implementation:

1. **Phase 1 - Permission Acquisition**
   ```xml
   <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />
   <uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>
   ```

2. **Phase 2 - Service Creation**
   - Membuat service yang berjalan di background
   - Service tidak dapat dihentikan dengan mudah oleh user

3. **Phase 3 - Overlay Attack**
   - Membuat window overlay yang menutupi seluruh layar
   - Menggunakan `TYPE_SYSTEM_ALERT` atau `TYPE_SYSTEM_OVERLAY`

4. **Phase 4 - User Interaction Block**
   - Menangkap semua input user (touch, back button, home button)
   - Mencegah akses ke aplikasi lain

---

## 🔧 Instalasi dan Penggunaan

### Prerequisites
- Android device dengan versi < 8.0
- Enable "Unknown Sources" di Security Settings
- Termux (optional untuk advanced testing)

### Langkah Instalasi

#### Text Guide 1: Basic Installation

```bash
# 1. Clone repository
git clone https://github.com/REYHAN6610/PhalanxLocks

# 2. Masuk ke direktori
cd PhalanxLocks

# 3. Jalan kan script python
pip install -r hook.txt
python edit.py

# 4. Conversikan ke aplikasi
Berikan input yang di kirim script
Buka ApkTool M Conversikan ke aplikasi

# 4. Edit Aplikasi
Anda bisa mengedit aplikasi sepeti


```

## ScreenShot + Tutorial

### Setelah membuat aplikasi nya
![Step1](https://qu.ax/wwVsk.jpg)

### Buka Apk tools M dan cari dimana anda menaruh folder BuildApp
![Step2](https://qu.ax/aSoCY.jpg)

### Jika sudah di decompile anda bisa click aplikasi nya
![Step2](https://qu.ax/lyfzD.jpg)

### Pilih Quick edit agar bisa di edit
![Step](https://qu.ax/PZXXF.jpg)

### Anda di sini bisa mengedit seperti icon dan nama aplikasi nya bebas
![Step](https://qu.ax/huyHV.jpg)

### Jika anda sudah puas anda bisa save jika eror menggunakan aapt bisa ganti jadi aapt2
![Step](https://qu.ax/EAiWa.jpg)



---

## 🤝 Kontributor

Terima kasih kepada semua platform dan tools yang memungkinkan pengembangan project edukasi ini:

<div align="center">

### Development Tools
[![Sketchware](https://img.shields.io/badge/Sketchware-App%20Development-blue?style=for-the-badge&logo=android)](https://sketchware.io)
[![GitHub](https://img.shields.io/badge/GitHub-Repository%20Hosting-black?style=for-the-badge&logo=github)](https://github.com)
[![Termux](https://img.shields.io/badge/Termux-Android%20Terminal-green?style=for-the-badge&logo=android)](https://termux.com)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-AI%20Assistant-orange?style=for-the-badge&logo=openai)](https://deepseek.com)

</div>

### Peran Masing-masing:

| Platform | Kontribusi |
|----------|------------|
| **Sketchware** | Pembuatan Ransomware di android |
| **GitHub** | Version control dan hosting repository |
| **Termux** | Untuk menjalankan dan membuat aplikasi menggunakan python |
| **DeepSeek** | AI assistance untuk dokumentasi dan coding |


---

<div align="center">

**⚠️ REMEMBER: Use Responsibly for Educational Purposes Only ⚠️**

*"With great power comes great responsibility" - Use this knowledge to protect, not to harm*

</div>
