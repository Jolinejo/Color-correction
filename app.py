""" Starts a Flask Web Application """
import os
from flask import Flask, request, render_template, jsonify
from daltonize import daltonize
import numpy as np
from PIL import Image
from flask_cors import CORS
import base64


def enhance(src, typ):
    """enhancment function
    recievies image
    returns enhanced image
    """
    orig_img = np.asarray(Image.open(src).convert("RGB"), dtype=np.float16)
    dl = daltonize
    orig_img = dl.gamma_correction(orig_img, 2.4)
    dalton_rgb = dl.daltonize(orig_img, typ)
    dalton_img = dl.array_to_img(dalton_rgb, 2.4)
    return (dalton_img)


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/upload/<typ>', methods=['POST'])
def upload_image(typ):
    """ sends image to func and returns edited image"""
    image = request.files['image']
    name = "imagebfore.jpg"
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
    processed = enhance(os.path.join(app.config['UPLOAD_FOLDER'], name), typ)
    processed.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
    with open(os.path.join(app.config['UPLOAD_FOLDER'], name), "rb") as file:
        encoded_string = base64.b64encode(file.read())
        return {"image": encoded_string.decode('utf-8')}

@app.route('/')
def index():
    return render_template('index.html')


cors = CORS(app, resources={r"/upload/*": {"origins": "*"}})
if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5001)
