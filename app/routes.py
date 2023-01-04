from app import app
from app.controllers.home_controller import HomeController


@app.route('/', methods=["GET"])
def test():
    return HomeController.index()
