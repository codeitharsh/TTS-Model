import torch
from TTS.api import TTS
from pydub import AudioSegment
import os
import sounddevice as sd
import numpy as np
import wave
import threading

# 🎤 Function to record audio with manual stop
def record_audio(filename, samplerate=22050):
    print("\n🎤 Recording... Press ENTER to stop.")

    recording = []
    stop_recording = threading.Event()

    def input_thread():
        input()  # Wait for user to press ENTER
        stop_recording.set()

    threading.Thread(target=input_thread, daemon=True).start()

    with sd.InputStream(samplerate=samplerate, channels=1, dtype='int16') as stream:
        while not stop_recording.is_set():
            data, _ = stream.read(1024)  # Read audio in chunks
            recording.append(data)

    print("✅ Recording stopped.")

    # Convert list of arrays to a single numpy array
    audio_data = np.concatenate(recording, axis=0)

    # Save as a WAV file
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)  
        wf.setsampwidth(2)  # 16-bit PCM
        wf.setframerate(samplerate)
        wf.writeframes(audio_data.tobytes())

# 🌍 Choose a language
print("\n🌍 Choose a language:")
print("1️⃣ English")
print("2️⃣ Hindi")
print("3️⃣ Both (English + Hindi)")
lang_choice = input("Enter 1, 2, or 3: ").strip()

if lang_choice == "1":
    language = "en"
elif lang_choice == "2":
    language = "hi"
elif lang_choice == "3":
    language = "hi"  # XTTS v2 supports multilingual output
else:
    print("❌ Invalid choice. Exiting.")
    exit()

# 📝 Get text input from the user
print("\n📝 Enter the text you want to convert to speech:")
text = input("> ")

# 🎙️ Predefined voice samples
preloaded_voices = {
    "1": r"C:\Users\Harsh\Desktop\TTS\Male_Voice.mp3",
    "2": r"C:\Users\Harsh\Desktop\TTS\Female_Voice.mp3"
}

# 🎙️ Ask the user to choose a voice
print("\n🎙️ Choose a voice sample:")
print("1️⃣ Male Voice")
print("2️⃣ Female Voice")
print("3️⃣ Record Now (Custom Voice)")
voice_choice = input("Enter 1, 2, or 3: ").strip()

if voice_choice in preloaded_voices:
    training_audio = preloaded_voices[voice_choice]
elif voice_choice == "3":
    training_audio = "custom_recording.wav"
    record_audio(training_audio)
else:
    print("❌ Invalid choice. Exiting.")
    exit()

# ⚙️ Set FFmpeg Path
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"

# 🖥️ Select device (GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"

# 🎤 Load XTTS v2 Model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# 🎶 Generate expressive speech
output_wav = "output.wav"
print("\n🗣️ Generating speech with **emotion and expression**...")
tts.tts_to_file(text=text, speaker_wav=training_audio, language=language, file_path=output_wav)

# 🎵 Convert WAV to MP3
output_mp3 = "output.mp3"
audio = AudioSegment.from_wav(output_wav)
audio.export(output_mp3, format="mp3")

# 🗑️ Remove temporary WAV file
os.remove(output_wav)

print(f"\n✅ MP3 file generated successfully: {output_mp3}")
