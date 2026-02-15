# YouTube Mashup Generator - Project Documentation

## Overview
The Mashup Generator is a Python-based audio processing application that automatically creates mashups from YouTube videos of one or more artists. The system provides both a command-line interface and a web-based interface for user interaction.

## Methodology
The Mashup Generator follows a structured six-step pipeline approach:

1. **Input Collection** - User provides singer name, number of videos (N > 10), duration (Y > 20), and email address.
2. **Video Downloading** - System searches YouTube using `yt-dlp` and downloads specified videos to `downloads/`.
3. **Audio Extraction** - FFmpeg extracts audio and trims each file to user-defined duration.
4. **Audio Merging** - All audio clips are combined into a single mashup file using FFmpeg/Pydub.
5. **Email Delivery** - Final mashup is compressed to ZIP format and sent via Gmail SMTP.
6. **User Feedback** - Web interface displays processing status, completion message, or error notifications.

### Methodology Flowchart
[Image of a six-step pipeline flowchart for a YouTube audio mashup generator]

## System Architecture
The system is organized into modular components to ensure flexibility and clean code:

* `mashup_core.py` - Core processing logic (Download, Trim, Merge).
* `102303183.py` - Command line version implementation.
* `webapp/` - Folder containing the Flask web application.

## Installation and Setup
### Prerequisites
* Python 3.7 or higher
* FFmpeg installed and accessible in system PATH
* Gmail account for email functionality (web version)

### Required Python Packages
```bash
pip install yt-dlp flask pydub python-dotenv


python 102303183.py "<Artist Name>" <num_videos> <duration> <output_file>
