from functionalities import *
from flask_cors import CORS

from flask import Flask

app = Flask(__name__)
CORS(app)

@app.route("/")
def getSlides():
    slides = all_slide()
    return slides
app.run()