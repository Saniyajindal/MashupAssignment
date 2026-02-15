# 🎵 YouTube Mashup Generator – Project Documentation  

## 📌 Overview  
The **YouTube Mashup Generator** is a Python-based audio processing application that automatically creates mashups from YouTube videos of a specified artist.  

The system provides:  
- 🖥️ Command-Line Interface (CLI)  
- 🌐 Web-Based Interface (Flask Application)  

Users can input the artist name, number of videos, and duration. The system downloads, processes, merges, and emails the final mashup automatically.

---

## ⚙️ Methodology  

The Mashup Generator follows a structured **six-step pipeline architecture**:

1. **Input Collection**  
   - Singer Name  
   - Number of Videos (N > 10)  
   - Duration in seconds (Y > 20)  
   - Email Address  

2. **Video Downloading**  
   - Uses `yt-dlp` to search and download videos from YouTube  
   - Files stored in the `downloads/` directory  

3. **Audio Extraction & Trimming**  
   - Uses **FFmpeg**  
   - Extracts audio from video files  
   - Trims each audio file to the specified duration  

4. **Audio Merging**  
   - Combines all trimmed clips  
   - Uses **FFmpeg / Pydub**  
   - Generates a single mashup file  

5. **Email Delivery**  
   - Final mashup compressed into ZIP format  
   - Sent to user via **Gmail SMTP**  

6. **User Feedback**  
   - Web interface displays:
     - Processing status  
     - Completion message  
     - Error notifications  

---

## 🖼️ Web Interface  

Below is the screenshot of the web application interface:

![Mashup Web Service UI](Interface)

---

## 🏗️ System Architecture  

| File / Folder | Description |
|---------------|------------|
| `mashup_core.py` | Core logic for Download, Trim, and Merge |
| `102303183.py` | Command-line version implementation |
| `webapp/` | Flask-based web application |
| `downloads/` | Stores downloaded YouTube videos |
| `output/` | Stores final mashup files |

---

## 🛠️ Installation and Setup  

### 🔹 Prerequisites  

- Python 3.7 or higher  
- FFmpeg installed and added to system PATH  
- Gmail account (for email feature in web version)  

---

### 🔹 Required Python Packages  

```bash
pip install yt-dlp flask pydub python-dotenv
