from flask import Flask, render_template, request, send_file
import os
import zipfile
import subprocess

app = Flask(__name__)

# Basic Form [cite: 28, 30, 32, 33, 35]
@app.route('/')
def index():
    return '''
    <h2>Mashup Web Service</h2>
    <form action="/process" method="post">
        Singer Name: <input type="text" name="singer" required><br><br>
        # of videos: <input type="number" name="n" min="11" required><br><br>
        Duration (sec): <input type="number" name="y" min="21" required><br><br>
        Email Id: <input type="email" name="email" required><br><br>
        <input type="submit" value="Submit">
    </form>
    '''

@app.route('/process', methods=['POST'])
def process():
    singer = request.form['singer']
    n = request.form['n']
    y = request.form['y']
    email = request.form['email']
    
    output_mp3 = "result.mp3"
    zip_name = "mashup_result.zip"

    try:
        # Program 1 (102303183.py) ko run karna [cite: 12]
        subprocess.run(["python", "102303183.py", singer, n, y, output_mp3], check=True)

        # File ko ZIP format mein convert karna 
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            zipf.write(output_mp3)

        # Result send karna 
        return send_file(zip_name, as_attachment=True)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)