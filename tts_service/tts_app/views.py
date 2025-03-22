from django.shortcuts import render

# Create your views here.
def home(requests):
    """
    Purpose: 
    """
    return render(requests,"tts_app/Navbar.html")

    
# end def

# from django.shortcuts import render
# from TTS.api import TTS

# def generate_tts(request):
#     if request.method == 'POST':
#         text = request.POST['text']
#         voice_id = request.POST['voice_id']
#         tts = TTS("tts_models/en/ljspeech/tacotron2-DDC").to("cuda" if torch.cuda.is_available() else "cpu")
#         audio_path = "output.wav"
#         tts.tts_to_file(text=text, file_path=audio_path)
#         return render(request, 'tts_app/result.html', {'audio': audio_path})
#     return render(request, 'tts_app/form.html')