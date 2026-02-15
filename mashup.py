import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment

# Step 2, 3 & 4: Core Logic for Audio Processing
def process_mashup(singer, n, y, output_name):
    # Temp folder create karna downloads ke liye
    if not os.path.exists('downloads'): 
        os.makedirs('downloads')
    
    # 1. Video Downloading using yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3'}],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True
    }
    
    print(f"Searching and downloading {n} videos for {singer}...")
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch{n}:{singer} songs"])

    # 2. Audio Extraction and Trimming
    combined = AudioSegment.empty()
    files = [f for f in os.listdir('downloads') if f.endswith('.mp3')][:n]
    
    print("Trimming and merging audio clips...")
    for file in files:
        audio = AudioSegment.from_file(os.path.join('downloads', file))
        # Step 3: FFmpeg extracts and trims to user-defined duration
        combined += audio[:y * 1000] 
    
    # 3. Audio Merging into a single output file
    combined.export(output_name, format="mp3")
    return output_name