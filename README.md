# MashupAssignment
# YouTube Audio Mashup Service

## Description
This project is a Python-based utility that creates a mashup of audio clips from YouTube videos of a specific singer. It includes both a command-line tool and a web service.

## Project Structure
- [cite_start]`102303183.py`: Command-line program to download, trim, and merge audio[cite: 12].
- [cite_start]`app.py`: Flask-based web service for the mashup[cite: 27].
- `requirements.txt`: List of required Python libraries.

## Features
- **Command Line Usage**: Run the script using the following format:
  [cite_start]`python 102303183.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>`[cite: 22].
- [cite_start]**Web Interface**: A user-friendly form to input singer name, number of videos (N > 10), and duration (Y > 20)[cite: 16, 19, 36].
- [cite_start]**Output**: The result is provided as a merged audio file in ZIP format[cite: 37].

## Installation
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
