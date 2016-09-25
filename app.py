import os
from flask import Flask, render_template, request, url_for, send_from_directory, redirect
from werkzeug import secure_filename

UPLOAD_FOLDER = "/tmp"
ALLOWED_EXTENSIONS = set(['jpg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST"])
def upload():
    # If there is no image_file param
    if "image_file" not in request.files:
        return "", 400

    file = request.files["image_file"]

    # If the image_file param is empty
    if file.filename == "":
        return "", 400

    # Check that the file has an allowed extension
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return redirect(url_for("uploaded_file", filename=filename))

    else:
        return "", 400

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run()
