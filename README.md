# Audio_File_Transcription
This repository (Audio_Transcript) is a flask web app that transcribes audio recordings to test. It uses the IBM watson developer cloud speech recognition API to transcribe the audio  files.


## Installation
```
git clone https:/github.com/ave12345/Audio_Transcription.git
cd Audio_Transcript
pip install --editable "[FILE_PATH]"
```

## Cloud Requirements
```
In order to make a call to the IBM watson cloud for any service,
it is required that you sign up for an [IBM cloud developer Account] (https://console.bluemix.net/).
After registration, you request to access the Speech recognition Services after which some 
credentials would be generated foryou and stored in the form of a json file
```


## Using The Cresentials
```
In the json file copy the username value and paste it in the username
attribute of the "app.config.update" method found in the Audio_Transcript.py file.
Do the same for the password.
```


## Starting Server
```
set FLASK_APP=Audio_Transcript.py
set FLASK_DEBUG=true
flask run
```

## Running Application
```
1. open your web browser
2. enter "localhost:5000" in your address bar (without the qoutes)
3. select a file and click Transcribe
NB1: audio file format can only be any of these (.wav, .flac, .mp3, .basic, .l16, .mpeg,
    .mulaw, .ogg, .webm)

NB2: The IBM Watson speech recognition websocket (used to make a request to the IBM cloud to 
transcribe audio files) is designed in such way that it can only transcribe one or a bunch 
of audios at a time. Hence, it is required that you unfortunaly have to restart you app's 
server after every transcription.
```
  

    
