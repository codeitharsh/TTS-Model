import os
import time
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(requests):
    """
    Purpose: 
    """
    return render(requests,"base.html")

    
# end def


def generate_speech(request):
    audio_url = None
    if request.method == 'POST':
        text = request.POST['text']
        # tts = TTS(model_name='tts_models/en/ljspeech/tacotron2-DCA')
        audio_filename = f"output.wav"
        audio_path = os.path.join(settings.MEDIA_ROOT, audio_filename)
        # tts.tts_to_file(text=text, file_path=audio_path)
        audio_url = settings.MEDIA_URL + audio_filename
    return render(request, 'tts_app/generate_speech.html', {'audio_url': audio_url})

def generate_clone_speech(requests):
    """
    Purpose: 
    """
    return "generate_clone_speech"
# end def