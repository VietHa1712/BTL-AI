from flask import Flask, request, jsonify, render_template
from color_recognition_api import knn_classifier
from color_recognition_api import color_histogram_feature_extraction
import numpy as np
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'message': 'No image selected'})
    image = request.files['image']
    nparr = np.frombuffer(image.read(), np.uint8)
    try:
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        color_histogram_feature_extraction.color_histogram_of_test_image(img_np)
        prediction = knn_classifier.main('training.data', 'test.data')
        message = f'Color predicted: {prediction.upper()}'
        return jsonify({'message': message})
    except:
        return jsonify({'message': 'Chosen file is not an image'})


if __name__ == '__main__':
    app.run()
