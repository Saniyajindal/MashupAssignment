from flask import Flask, render_template, request, send_file
import os, zipfile
from mashup_core import process_mashup

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') # Iska sundar UI nichhe hai

@app.route('/process', methods=['POST'])
def process():
    singer = request.form.get('singer')
    n = int(request.form.get('n'))
    y = int(request.form.get('y'))
    email = request.form.get('email')
    
    output_mp3 = "final_mashup.mp3"
    zip_name = "mashup.zip"

    try:
        process_mashup(singer, n, y, output_mp3)
        with zipfile.ZipFile(zip_name, 'w') as z:
            z.write(output_mp3)
        
        # Note: Actual Email sending ke liye SMTP config chahiye hogi
        return send_file(zip_name, as_attachment=True) 
    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
