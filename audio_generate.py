from pydub import AudioSegment
import os

# Define paths to input files
speech_path = "google.mp3"
music_path = "back.mp3"
output_path = "output_with_intro_music.mp3"

# Check if input files exist
if not os.path.isfile(speech_path):
    print(f"Speech file not found: {speech_path}")
    exit(1)
if not os.path.isfile(music_path):
    print(f"Music file not found: {music_path}")
    exit(1)

# Load the synthesized speech
speech = AudioSegment.from_file(speech_path)

# Load the background music
intro_music = AudioSegment.from_file(music_path)

# Trim the intro music to 10 seconds (10000 milliseconds)
intro_music_trimmed = intro_music[:8000]

# Apply a fade-out effect over the entire duration of the trimmed intro music
intro_music_faded = intro_music_trimmed.fade_out(duration=8000)

# Combine intro music with speech
combined = intro_music_faded + speech

# Export the combined audio
combined.export(output_path, format="mp3")
print(f'Audio with intro music written to file "{output_path}"')
