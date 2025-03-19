import torch
from TTS.api import TTS
from pydub import AudioSegment  # For WAV to MP3 conversion
import os

# Set ffmpeg path for pydub (update this to your actual path)
AudioSegment.converter = "C:\\Path\\To\\ffmpeg.exe"  # Replace with real path

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Initialize the TTS model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Define input text and reference audio
text = "Hello world! This is a test of Coqui TTS."
speaker_wav = "my_cloning/audio.wav"  # Ensure this file exists
language = "en"

# Generate speech and save as WAV
output_wav = "output.wav"
tts.tts_to_file(text=text, speaker_wav=speaker_wav, language=language, file_path=output_wav)

# Convert WAV to MP3
output_mp3 = "output.mp3"
audio = AudioSegment.from_wav(output_wav)
audio.export(output_mp3, format="mp3")

# Optional: Clean up
os.remove(output_wav)

print(f"MP3 file generated successfully: {output_mp3}")