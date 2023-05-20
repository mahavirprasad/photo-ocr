import pytesseract
from PIL import Image
from flask import Flask, request

app = Flask(__name__)

@app.route("web-photo-ocr.py", methods=["POST"])
def process_image():
    image_file = request.files["image"]
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)

    return text

if __name__ == "__main__":
    app.run(host="localhost", port=8000)
