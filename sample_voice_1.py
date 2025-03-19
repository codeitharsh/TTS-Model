import torch
from TTS.api import TTS
from pydub import AudioSegment
import os

# Set ffmpeg path (update this to your actual path)
AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"  # Replace with your ffmpeg path

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Initialize the TTS model (single-speaker)
tts = TTS("tts_models/en/ljspeech/tacotron2-DDC").to(device)

# Define input text
text = """The wind roared in Alex's ears as he stood at the edge of the skyscraper. Thirty stories high. The neon city below pulsed like a living thing.

Behind him, the footsteps were getting closer. Too close.

“No turning back now,” he muttered, tightening his grip on the stolen drive. The evidence that could bring down the whole syndicate.

A gun cocked. “End of the line, Alex.”

He grinned. “Not quite.”

With a deep breath, he sprinted forward—and leaped.

For a heartbeat, he was weightless. Then—CRASH!—he landed on the rooftop below, rolling hard but laughing as sirens filled the air.

He was alive. And the game had just begun."""

# Generate speech and save as WAV
output_wav = "output.wav"
tts.tts_to_file(text=text, file_path=output_wav)

# Convert WAV to MP3
output_mp3 = "output.mp3"
audio = AudioSegment.from_wav(output_wav)
audio.export(output_mp3, format="mp3")

# Clean up
os.remove(output_wav)

print(f"MP3 file generated successfully: {output_mp3}")
