from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['image_file']
    filename = secure_filename(file.filename)
    return filename

if __name__ == "__main__":
    app.run()
