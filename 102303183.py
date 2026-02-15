import sys
import os
from yt_dlp import YoutubeDL
from pydub import AudioSegment

def create_mashup(singer, n, duration, output):
    # Temporary folder for storage
    if not os.path.exists('temp_files'):
        os.makedirs('temp_files')

    # 1. Download & Convert [cite: 16, 17, 18]
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3'}],
        'outtmpl': 'temp_files/%(title)s.%(ext)s',
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch{n}:{singer}"])

    # 2. Trim and Merge [cite: 19, 20]
    combined = AudioSegment.empty()
    files = [f for f in os.listdir('temp_files') if f.endswith('.mp3')]
    
    for file in files[:n]:
        audio = AudioSegment.from_file(os.path.join('temp_files', file))
        trimmed = audio[:duration * 1000] # Y seconds cut [cite: 19]
        combined += trimmed

    # 3. Final Output
    combined.export(output, format="mp3")
    print(f"Done! Mashup saved as {output}")

if __name__ == "__main__":
    # Param check [cite: 23, 24, 25]
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <SingerName> <NumVideos> <Duration> <OutputFileName>") [cite: 22]
        sys.exit(1)

    try:
        # Constraints: N > 10, Y > 20 [cite: 16, 19]
        singer = sys.argv[1]
        n = int(sys.argv[2])
        y = int(sys.argv[3])
        out = sys.argv[4]
        
        create_mashup(singer, n, y, out)
    except Exception as e:
        print(f"Error: {e}") [cite: 26]