from flask import Flask, render_template, request, send_file
import os, zipfile, subprocess

app = Flask(__name__)

@app.route('/')
def home():
    # Requirements: Singer, # of videos, duration, email [cite: 28, 30, 32, 33]
    return '''
    <form action="/process" method="post">
        Singer: <input name="singer"><br>
        Videos (N > 10): <input name="n" type="number"><br>
        Duration (Y > 20): <input name="y" type="number"><br>
        Email: <input name="email" type="email"><br>
        <input type="submit">
    </form>
    '''

@app.route('/process', methods=['POST'])
def process():
    # Process and send as ZIP [cite: 37]
    # Logic to trigger 102303183.py and zip the result
    return "Process started. Result will be zipped and sent."

if __name__ == "__main__":
    app.run(debug=True)
