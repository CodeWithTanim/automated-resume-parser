# app/routes.py

from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
import os
from .parser import extract_resume_data
from .utils import save_parsed_data
from config import UPLOAD_FOLDER

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    parsed_data = None

    if request.method == 'POST':
        if 'resume' not in request.files:
            return render_template('index.html', error="No file part")

        file = request.files['resume']

        if file.filename == '':
            return render_template('index.html', error="No selected file")

        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)

            # Extract data from resume
            parsed_data = extract_resume_data(file_path)

            # Save parsed data (optional)
            save_parsed_data(parsed_data, filename)

            return render_template('index.html', parsed_data=parsed_data)

    return render_template('index.html', parsed_data=parsed_data)
