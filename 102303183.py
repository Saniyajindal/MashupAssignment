import sys
from mashup_core import process_mashup

if __name__ == "__main__":
    # [cite_start]Parameters check [cite: 23, 24]
    if len(sys.argv) != 5:
        [cite_start]print("Usage: python 102303183.py <SingerName> <N> <Y> <OutputName>") [cite: 22]
        sys.exit(1)

    try:
        singer, n, y, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
        
        # [cite_start]Validation for N > 10 and Y > 20 [cite: 16, 19]
        if n <= 10 or y <= 20:
            print("Error: N must be > 10 and Y must be > 20.")
            sys.exit(1)
            
        print("Starting Mashup Process...")
        process_mashup(singer, n, y, out)
        print("Mashup created successfully.")
        
    except Exception as e:
        [cite_start]print(f"Error: {e}") [cite: 26]
