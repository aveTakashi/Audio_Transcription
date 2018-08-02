import pytest
from Audio import Audio
import flask
app = flask.Flask(__name__)
from io import BytesIO

@pytest.fixture
def client():
    Audio.app.config["TESTING"] = True
    client = Audio.app.test_client()
    yield client



#requesting a post method with file upload
def transcribe_audio_file(client, file_path):
    data = {
        'file_path' : (BytesIO(b'FILE CONTENT'), file_path)
    }
    return client.post("/transcribe", data=data, follow_redirects=True, content_type='multipart/form-data')





        
def test_file_not_selected(client):
    rv = transcribe_audio_file(client,"")
    assert b'Please select an audio file' in rv.data


def test_audio_transcription(client):
    transcribe_audio_file(client, "audio2.flac")
    assert Audio.app.config["DATA"] =="the latest weather report "

