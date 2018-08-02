from flask import Flask, request, render_template, redirect, url_for, flash
from watson_developer_cloud import SpeechToTextV1
from werkzeug.utils import secure_filename
import io
import json

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(
    SECRET_KEY = b'as&%jksd$?hsg',
    DATA = "",
    watson_api = SpeechToTextV1(
        username="289a0d22-d36d-40ae-a398-6375e0275d85",
        password="8JQdnFWtR6sv",
        url="https://stream.watsonplatform.net/speech-to-text/api"
    )
)

@app.route("/")
def Index():
    return render_template("Index.html", data=app.config["DATA"])


@app.route("/transcribe", methods=["POST","GET"])
def transcribe_audio_file():
    print(request.files)
    if request.files:
        f = request.files['file_path']

        audio_file = secure_filename(f.filename)
        aud_type = get_file_extension(audio_file)
        watson_api = app.config["watson_api"]

    
        response = read_audio_file(audio_file,watson_api,aud_type)
        app.config["DATA"] = response["results"][0]["alternatives"][0]["transcript"]
        

        return redirect(url_for("Index",data=app.config["DATA"]))

    else:
        flash("Please select an audio file")
        return redirect(url_for('Index'))



def read_audio_file(audio_file,watson_api,aud_type):
    with io.open(audio_file, "rb") as audio_bytes:
        response = watson_api.recognize(
            audio= audio_bytes,
            content_type = "audio/"+aud_type,
            model = "en-US_BroadbandModel",
            timestamps= True
        )
        return response



def get_file_extension(file_name):
    extension =""
    for i in range(len(file_name)):
        if file_name[-i-1]!=".":
            extension += file_name[-i-1]
        else:
            return extension[::-1]