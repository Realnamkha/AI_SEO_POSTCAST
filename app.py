
"""Synthesizes speech from the input string of text."""
from google.cloud import texttospeech
import os 
INPUT_PATH = "main.txt" 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'google_cloud.json'

with open(INPUT_PATH, 'r', encoding='utf-8') as f:
    main_text = f.read()
client = texttospeech.TextToSpeechClient()

input_text = texttospeech.SynthesisInput(text=main_text)

# Note: the voice can also be specified by name.
# Names of voices can be retrieved with client.list_voices().
voice = texttospeech.VoiceSelectionParams(
    language_code="en-GB",
    name="en-GB-Neural2-D",
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16,
    speaking_rate=1
)

response = client.synthesize_speech(
    request={"input": input_text, "voice": voice, "audio_config": audio_config}
)

# The response's audio_content is binary.
with open("google.mp3", "wb") as out:
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')