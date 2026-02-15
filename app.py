from flask import Flask, render_template, request, send_file
import os, zipfile
import sys
sys.path.append('..') # Core logic ko access karne ke liye
from mashup_core import process_mashup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    singer = request.form.get('singer')
    n = int(request.form.get('n'))
    y = int(request.form.get('y'))
    [cite_start]email = request.form.get('email') # Must be correct [cite: 38]
    
    output_mp3 = "result.mp3"
    zip_name = "mashup.zip"

    try:
        process_mashup(singer, n, y, output_mp3)
        # [cite_start]Result file in zip format [cite: 37]
        with zipfile.ZipFile(zip_name, 'w') as z:
            z.write(output_mp3)
        
        return send_file(zip_name, as_attachment=True) 
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
