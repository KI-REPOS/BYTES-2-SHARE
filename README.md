# BYTE - Local Wi-Fi File Sharing Web App

A Django-based local FTP-style file sharing application that lets devices connected to the same Wi-Fi network upload, share, and download files of **any type and size** directly from a centralized storage pool hosted on a laptop.

---

## 🚀 Features

- **Unlimited file size support** — upload any file type with no restrictions
- **Chunked, resumable uploads** — reliable transfer of large files without starting over if interrupted
- **User authentication** — only registered users can upload; downloads are public
- **Bootstrap UI (offline)** — responsive, modern design works without internet
- **Progress bar for uploads** — shows percentage complete and estimated time remaining
- **Landing page** with two simple options: **Download** and **Upload**
- **File list view** — see all stored files with size, date, and download button
- **Accessible from any device** on the same local Wi-Fi (laptop, phone, tablet, etc.)
- Optional **QR code** for instant mobile access

---

## 📂 Use Cases

- Home/office file sharing without cloud dependency
- Quick transfer between laptop and mobile devices
- Temporary shared file drop zone for events, classrooms, or teams
- Share large videos, documents, or software installers locally

---

## 🛠 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/KI-REPOS/BYTES-2-SHARE
```
### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run migrations
```bash
python manage.py migrate
```
### 4️⃣ Start the server (local network mode)
```bash
python manage.py runserver 0.0.0.0:8000
```
### Project Preview
Landing Page
<p align="center">
  <img width="1920" height="1080" alt="Screenshot 2025-08-12 172413" src="https://github.com/user-attachments/assets/a6a0d2cd-a680-4c2d-970a-76dd9b13ed87" />
</p>
Login Page
<p align="center">
  <img width="1920" height="1080" alt="Screenshot 2025-08-12 172436" src="https://github.com/user-attachments/assets/830a0792-2059-4ed2-a880-9bdf25c05b7d" />
</p>
Upload Page
<p align="center">
  <img width="1920" height="1080" alt="Screenshot 2025-08-12 172541" src="https://github.com/user-attachments/assets/3910a5e1-cf40-4c60-8fd6-912d2176b6e9" />
</p>
Download Page
<p align="center">
  <img width="1920" height="1080" alt="Screenshot 2025-08-12 172718" src="https://github.com/user-attachments/assets/370fb8d0-0033-474c-bef1-56af1546808b" />
</p>


