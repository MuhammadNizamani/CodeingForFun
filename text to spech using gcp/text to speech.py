import os
from google.cloud import texttospeech
from google.cloud import texttospeech_v1
from IPython.display import Audio
from playsound import playsound
import time
# this will work when you have api key of gcp

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'mvprun-auth-e1de5fad33d3.json'
clint = texttospeech_v1.TextToSpeechClient()

text = str(input("Enter any string :"))

synthesis_input = texttospeech_v1.SynthesisInput(text=text)
voice = texttospeech_v1.VoiceSelectionParams(language_code="en-GB", ssml_gender=texttospeech.SsmlVoiceGender.MALE)
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
response = clint.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

with open("output1.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')




time.sleep(3)
playsound("output1.mp3")
