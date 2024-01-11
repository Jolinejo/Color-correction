""" Starts a Flash Web Application """
from os import environ
from flask import Flask, request, render_template, jsonify
from daltonize import daltonize
import numpy as np
from PIL import Image
import cv2

def apply_inhancment(src):
    dst = cv2.imread(src)
    dl = daltonize
    orig_img = dl.gamma_correction(dst, 2.4)
    dalton_rgb = dl.daltonize(orig_img, 'p')
    dalton_img = dl.array_to_img(dalton_rgb, 2.4) 
    return (dalton_img)

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    """ sends image to func and returns edited image"""
    image = request.files['image']


    return render_template()


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)