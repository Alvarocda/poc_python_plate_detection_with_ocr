import argparse
import io
from PIL import Image

import torch
from flask import Flask, request


class DetectionController:
    def predict():

        model = torch.hub.load('ultralytics/yolov5', 'custom',
                               path='app/assets/best.pt', source='github')  # local repo
        print("Entrou no controller de predict")
        if not request.method == "POST":
            return

        if request.files.get("image"):
            image_file = request.files["image"]
            image_bytes = image_file.read()
            img = Image.open(io.BytesIO(image_bytes))
            results = model(img, size=640)
            return results.pandas().xyxy[0].to_json(orient="records")
