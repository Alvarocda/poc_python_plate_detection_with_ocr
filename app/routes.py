from app import app
from app.controllers.detection_controller import DetectionController


@app.route("/predict", methods=["POST"])
def predict():
    return DetectionController.predict()
