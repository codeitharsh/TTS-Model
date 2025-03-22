import torch
from TTS.api import TTS
from pydub import AudioSegment
import os

# Set ffmpeg path (update this to your actual path)
AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"  # Replace with your ffmpeg path

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Initialize the VITS model with VCTK dataset (multi-speaker)
tts = TTS("tts_models/en/vctk/vits").to(device)

# Define text segments for storytelling or conversation
story_segments = [
    {"text": "Once upon a time, in a faraway land, there lived a brave knight.", "speaker": "p225"},  # Male voice
    {"text": "He met a wise queen who spoke with grace and authority.", "speaker": "p226"},       # Female voice
    {"text": "Together, they planned to save the kingdom from a fierce dragon!", "speaker": "p227"}  # Another male voice
]

# Generate and save audio for each segment
output_files = []
for i, segment in enumerate(story_segments):
    output_wav = f"segment_{i}.wav"
    tts.tts_to_file(
        text=segment["text"],
        speaker=segment["speaker"],  # Specify different VCTK speaker IDs
        file_path=output_wav
    )
    output_files.append(output_wav)

# Combine segments into one WAV file
combined = AudioSegment.empty()
for wav_file in output_files:
    segment_audio = AudioSegment.from_wav(wav_file)
    combined += segment_audio

# Export combined audio as MP3
output_mp3 = "story_output.mp3"
combined.export(output_mp3, format="mp3")

# Clean up temporary WAV files
for wav_file in output_files:
    os.remove(wav_file)

print(f"MP3 file generated successfully: {output_mp3}")