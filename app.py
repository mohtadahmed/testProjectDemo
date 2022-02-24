from fileinput import filename
from importlib.resources import path
import os
from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle POST Request here
        if request.files:
            f = request.files['file']
            filename = secure_filename(f.filename)
            path = 'upload/file'
            filePath = os.path.join(path, filename)
            f.save(filePath)
            return render_template('home.html')
    return render_template('index.html')


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
