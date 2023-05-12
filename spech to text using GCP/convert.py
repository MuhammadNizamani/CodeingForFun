import os
# import io
from google.cloud import speech
# import json
import matplotlib.pyplot as plt
import numpy as np
import os
# import pandas as pd
# import requests
# import time
from base64 import b64encode
# from IPython.display import Audio
# from pylab import rcParams

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq = 48000

# Recording duration
duration = 7
print("start recording")
# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)

# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)
print("voice is done")

def speech_to_text():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']="D:\job work\Text to speech\mvprun-auth-218533c8a96a.json"
    # Audio("recording1.wav")
    clint = speech.SpeechClient()
    with open("recording1.wav", 'rb') as audio_file:
        content = audio_file.read()
        audio1 = speech.RecognitionAudio(content=content)

    config12 = speech.RecognitionConfig(encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16, sample_rate_hertz =  48000,language_code='en_us',audio_channel_count=2,enable_word_time_offsets=True)
    response = clint.recognize(config=config12,audio=audio1)
    for result in response.results:
        print(result.alternatives[0].transcript)


speech_to_text()


