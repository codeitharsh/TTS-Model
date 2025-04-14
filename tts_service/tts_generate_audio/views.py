import os
from django.http import JsonResponse, HttpResponse
from django.views import View
from TTS.api import TTS
import torch

# Initialize the TTS model (loaded once when the server starts)
device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

class GenerateSpeechView(View):
    def post(self, request):
        # Extract language, speaker, and text from the POST request
        language = request.POST.get('language')
        speaker = request.POST.get('speaker')
        text = request.POST.get('text')

        # Validate inputs
        if not language or not speaker or not text:
            return JsonResponse(
                {'error': 'Missing required parameters: language, speaker, or text'},
                status=400
            )

        # Check if the speaker is valid
        if speaker not in tts.speakers:
            return JsonResponse(
                {'error': f'Invalid speaker: {speaker}'},
                status=400
            )

        # Check if the language is supported
        if language not in tts.languages:
            return JsonResponse(
                {'error': f'Invalid language: {language}'},
                status=400
            )

        try:
            # Generate speech using the TTS API
            wav = tts.tts(text=text, speaker=speaker, language=language)

            # Save the audio to a temporary file
            output_file = os.path.join('/tmp', f"{speaker}_{language}.wav")
            tts.synthesizer.save_wav(wav, output_file)

            # Serve the audio file as a response
            with open(output_file, 'rb') as audio_file:
                response = HttpResponse(audio_file.read(), content_type="audio/wav")
                response['Content-Disposition'] = f'attachment; filename="{speaker}_{language}.wav"'
                return response

        except Exception as e:
            return JsonResponse(
                {'error': f'Failed to generate audio: {str(e)}'},
                status=500
            )