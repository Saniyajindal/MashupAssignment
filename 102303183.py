import sys
from mashup_core import process_mashup

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python 102303183.py <SingerName> <N> <Y> <OutputName>")
        sys.exit(1)

    try:
        singer, n, y, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
        if n <= 10 or y <= 20:
            print("Error: Input constraints failed (N > 10, Y > 20).")
            sys.exit(1)
            
        process_mashup(singer, n, y, out)
        print("Success: Mashup generated successfully!")
    except Exception as e:
        print(f"Runtime Error: {e}")
