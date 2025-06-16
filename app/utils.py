# app/utils.py

import os
import json
from config import PARSED_DATA_FOLDER

def save_parsed_data(data, original_filename):
    filename = os.path.splitext(original_filename)[0] + '.json'
    filepath = os.path.join(PARSED_DATA_FOLDER, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
