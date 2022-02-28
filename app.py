from fileinput import filename
from http.client import OK
from importlib.resources import path
import os
from flask import Flask, redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import PyPDF2


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle POST Request here
        if request.files:
            f = request.files['file']
            name = str(request.form['person'])
            filename = secure_filename(f.filename)
            path = 'upload/file/' + name
            # x = os.mkdir(path)

            # IF Else loop for checking the directory exists or not
            if os.path.isdir(path) == True:
                print(path)
            else:
                os.mkdir(path)

            # If Else Loop Ends

            print(path)
            filePath = os.path.join(path, filename)

            # IF Else loop for checking the same name file exists in the directory
            if os.path.isfile(filePath) == True:
                os.remove(filePath)
                print('work on IF')
                f.save(filePath)
            else:
                f.save(filePath)
                print('Work on Else')
            print(filePath)
            # IF Else loop for checking the same name file exists in the directory

            # Code for PDF Page Counter
            sample_pdf = open(filePath, mode='rb')
            pdfdoc = PyPDF2.PdfFileReader(sample_pdf)
            print(pdfdoc.numPages)
            pageNumber = pdfdoc.numPages
            # Code for PDF Page Counter

            return render_template('home.html', pageNumber=pageNumber)
    return render_template('index.html')


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
