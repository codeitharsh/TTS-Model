import os
import time
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.conf import settings

AUDIO_DIR = os.path.join(settings.MEDIA_ROOT, "Audio_XTTS_v2")

# Create your views here.
def home(requests):
    """
    Purpose: 
    """
    return render(requests,"tts_app/home.html")
# end def

def sign_in(requests):
    """
    Purpose: 
    """
    return render(requests,"tts_app/login.html")
    
# end def

def integrations(requests):
    """
    Purpose: arg
    """
    return render(requests,"tts_app/integrations.html")
    
# end def


def examples(requests):
    """
    Purpose: arg
    """
    return render(requests,"tts_app/examples.html")
    
# end def

def pricing(requests):
    """
    Purpose: arg
    """
    return render(requests,"tts_app/pricing.html")
    
# end def

def get_speakers(request):
    """Returns a list of available speakers from the media folder."""
    if not os.path.exists(AUDIO_DIR):
        return JsonResponse({"error": "Audio directory not found"}, status=404)
    
    speakers = [
        {"name": file.replace("tts_models_multilingual_multi-dataset_xtts_v2_", "").replace("_eng.wav", ""), 
         "file": file}
        for file in os.listdir(AUDIO_DIR) if file.endswith(".wav")
    ]
    
    return JsonResponse({"speakers": speakers})

def get_audio(request, filename):
    """Returns the selected audio file."""
    file_path = os.path.join(AUDIO_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, "rb"), content_type="audio/wav")
    return JsonResponse({"error": "File not found"}, status=404)
