import sys
import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment

def create_mashup(singer, n, duration, output):
    if not os.path.exists('temp'): os.makedirs('temp')

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3'}],
        'outtmpl': 'temp/%(title)s.%(ext)s',
    }
    
    # Download N videos [cite: 16, 17]
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch{n}:{singer}"])

    combined = AudioSegment.empty()
    files = [f for f in os.listdir('temp') if f.endswith('.mp3')][:n]
    
    for file in files:
        audio = AudioSegment.from_file(os.path.join('temp', file))
        # Trim first Y seconds 
        combined += audio[:duration * 1000] 
    
    # Export final audio 
    combined.export(output, format="mp3")

if __name__ == "__main__":
    # Command line usage check [cite: 21, 22]
    if len(sys.argv) != 5:
        print("Usage: python 102303183.py <SingerName> <N> <Y> <OutputName>")
        sys.exit(1)

    try:
        s, n, y, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
        if n <= 10 or y <= 20: # Constraints check [cite: 16, 19]
            print("Error: N > 10 and Y > 20")
            sys.exit(1)
        create_mashup(s, n, y, out)
    except Exception as e:
        print(f"Error: {e}") [cite: 26]
