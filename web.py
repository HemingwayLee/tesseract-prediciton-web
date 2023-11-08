import os
import json
from io import BytesIO
from PIL import Image
from flask import Flask
import pytesseract

print(pytesseract.image_to_string(Image.open('images/jp.png'), lang="jpn"))

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/ocr/image_bytes/')
def run_image_byte():
    image_bytes = request.data
    image_data = BytesIO(image_bytes)
    image = Image.open(image_data)
    res = pytesseract.image_to_string(image, lang="jpn")

    return json.dumps({"predictions": res})

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)

