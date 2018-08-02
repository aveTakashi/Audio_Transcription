# Audio_Transcription
This repository (Audio_Transcript) is a flask web app that transcribes audio recordings to test. It uses the IBM watson developer cloud speech recognition API to transcribe the audio  files.


## Installation
```
git clone https://github.com/ave12345/Audio_Transcription.git
cd Audio_Transcription
[optional] mkvirtualenv Audio_Transcription
pip install -r requirements.txt
```

## Cloud Requirements
```
In order to make a call to the IBM watson cloud for any service,
it is required that you sign up for an [IBM Watson cloud developer Account] (https://console.bluemix.net/).
After registration, you request to access the Speech recognition Services after which some 
credentials would be generated for you and stored in the form of a json file
```


## Using The Cresentials
```
In the json file copy the username value and paste it in the username
attribute of the "app.config.update" method found in the Audio.py file.
Do the same for the password.
```


## Starting Server
```
[In your terminal execute:]
set FLASK_APP=Audio.py
flask run
```

## Running Application
```
1. open your web browser
2. enter "localhost:5000" in your address bar (without the qoutes)
3. select a file and click Transcribe [ There are sample audio files in the project directory for testing purpose]
NB1: audio file format can only be any of these (.wav, .flac, .mp3, .basic, .l16, .mpeg,
    .mulaw, .ogg, .webm)
```
  

    
