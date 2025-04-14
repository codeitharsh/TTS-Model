from django.http import HttpResponse, JsonResponse
from django.views import View
from .tts_generator import TTSGenerator
from django.conf import settings
import os
import tempfile

# Define preloaded voices (ensure these files exist in your media directory)
PRELOADED_VOICES = {
    "male": os.path.join(settings.MEDIA_ROOT, "voices", "Male_Voice.mp3"),
    "female": os.path.join(settings.MEDIA_ROOT, "voices", "Female_Voice.mp3"),
}

# Initialize TTSGenerator (singleton instance for efficiency)
tts_generator = TTSGenerator(PRELOADED_VOICES)

class GenerateSpeechView(View):
    def post(self, request):
        """
        Handle POST request to generate speech from user input.
        """
        # Extract form data
        language = request.POST.get('language')
        text = request.POST.get('text')
        voice_choice = request.POST.get('voice_choice')
        custom_voice = request.FILES.get('custom_voice')

        # Validate inputs
        if not all([language, text, voice_choice]):
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        valid_languages = ['en', 'hi', 'both']
        valid_voices = ['male', 'female', 'custom']
        if language not in valid_languages:
            return JsonResponse({'error': 'Invalid language choice'}, status=400)
        if voice_choice not in valid_voices:
            return JsonResponse({'error': 'Invalid voice choice'}, status=400)
        if voice_choice == 'custom' and not custom_voice:
            return JsonResponse({'error': 'Custom voice file is required'}, status=400)

        custom_voice_path = None
        try:
            # Handle custom voice upload
            if voice_choice == 'custom':
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
                    for chunk in custom_voice.chunks():
                        temp_file.write(chunk)
                    custom_voice_path = temp_file.name

            # Generate speech
            mp3_data = tts_generator.generate_speech(text, language, voice_choice, custom_voice_path)

            # Return MP3 as a response
            response = HttpResponse(mp3_data, content_type='audio/mpeg')
            response['Content-Disposition'] = 'attachment; filename="output.mp3"'
            return response

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

        finally:
            # Clean up temporary custom voice file if it exists
            if custom_voice_path and os.path.exists(custom_voice_path):
                os.remove(custom_voice_path)