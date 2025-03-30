from django.shortcuts import render


# Create your views here.
def generate_speech(requests):
    """
    Purpose: 
    """
    return render(requests,"tts_generate_audio/generate_audio.html")
# end def

# import torch
# import io
# import base64
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from TTS.api import TTS

# # Load TTS model once for efficiency
# device = "cuda" if torch.cuda.is_available() else "cpu"
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=device == "cuda")

# @csrf_exempt
# def generate_speech(request):
#     if request.method == "POST":
#         try:
#             data = request.POST
#             text = data.get("text", "").strip()
#             speaker = data.get("speaker", "").strip()
#             language = data.get("language", "en").strip()

#             if not text or not speaker or not language:
#                 return JsonResponse({"error": "Missing parameters"}, status=400)

#             # Generate audio as bytes (in-memory)
#             audio_buffer = io.BytesIO()
#             tts.tts_to_file(
#                 text=text,
#                 speaker=speaker,
#                 language=language,
#                 file_path=audio_buffer
#             )

#             # Encode audio to base64 for direct playback
#             audio_base64 = base64.b64encode(audio_buffer.getvalue()).decode("utf-8")

#             return JsonResponse({"audio": f"data:audio/wav;base64,{audio_base64}"})

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)
    
#     return JsonResponse({"error": "Invalid request"}, status=400)
