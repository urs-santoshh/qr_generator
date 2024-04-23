from flask import Flask, request, render_template
import os
import json
from .qr import generate_qr

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template('home.html')

@app.route("/postform", methods=["POST"])
def read_form():
    file = os.path.isfile("app/static/img/qr.png")
    if file:
        os.remove("app/static/img/qr.png")
    try:
        postData = request.form["userData"]
        if postData == "":
            message = {
                        "type":"Error",
                        "tags":"warning",
                        "detail":"empty data sent"
                    }
            return render_template("qr.html", message=message)
        usrData = json.loads(postData)
        generate_qr(usrData)
        message = {
                    "type":"Success",
                    "tags":"success",
                    "detail":"QR code generated successfully"
                }
        return render_template("qr.html", message=message)
    except Exception:
        message = {
                    "type":"Error",
                    "tags":"warning",
                    "detail":"plz send data in JSON format"
                }
        return render_template("qr.html", message=message)
