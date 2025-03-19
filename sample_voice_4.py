import torch
from TTS.api import TTS
from pydub import AudioSegment
import os

# Ensure ffmpeg is correctly set
ffmpeg_path = "C:\\ffmpeg\\bin\\ffmpeg.exe"  # Update with your actual ffmpeg path
AudioSegment.converter = ffmpeg_path

# Get available device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Choose an alternative phonemizer if needed (Disable espeak-ng)
try:
    tts = TTS("tts_models/en/vctk/vits", use_phonemes=False).to(device)
except Exception as e:
    print(f"Error loading TTS model: {e}")
    print("Trying alternative TTS model without phonemization...")
    tts = TTS("tts_models/en/ljspeech/tacotron2").to(device)  # Single-speaker fallback

# Define text segments with speakers
story_segments = [
    {"text": "Late one evening, Liam found himself walking home through the dense fog that had rolled into the quiet town.", "speaker": "p225"},  # Narrator (male)
    {"text": "Then, he heard it. A voice—soft, melodic—whispering his name.", "speaker": "p225"},
    {"text": "Liam...", "speaker": "p226"},  # Ghostly woman (female)
    {"text": "He stopped, heart pounding.", "speaker": "p225"},
    {"text": "Who's there?", "speaker": "p227"},  # Liam (another male voice)
    {"text": "Help me...", "speaker": "p226"},  # Ghostly woman
    {"text": "Taking a deep breath, Liam stepped onto the bridge.", "speaker": "p225"},
    {"text": "A figure emerged—faint, glowing. A young woman with sorrowful eyes.", "speaker": "p225"},
    {"text": "You can hear me?", "speaker": "p226"},
    {"text": "A voice from the past… one that was never heard.", "speaker": "p226"}
]

# Generate and save audio for each segment
output_files = []
for i, segment in enumerate(story_segments):
    output_wav = f"segment_{i}.wav"
    try:
        tts.tts_to_file(text=segment["text"], speaker=segment["speaker"], file_path=output_wav)
        output_files.append(output_wav)
    except Exception as e:
        print(f"Error generating audio for segment {i}: {e}")

# Combine all segments into one audio file
combined = AudioSegment.empty()
for wav_file in output_files:
    try:
        segment_audio = AudioSegment.from_wav(wav_file)
        combined += segment_audio
    except Exception as e:
        print(f"Error processing {wav_file}: {e}")

# Export final MP3
output_mp3 = "story_output.mp3"
combined.export(output_mp3, format="mp3")

# Cleanup temporary WAV files
for wav_file in output_files:
    os.remove(wav_file)

print(f"MP3 file generated successfully: {output_mp3}")
