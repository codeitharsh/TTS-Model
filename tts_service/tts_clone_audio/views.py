from django.shortcuts import render

# Create your views here.
def clone_speech(request):
    """
    Purpose: 
    """
    return  render(request=request,template_name="tts_clone_audio/coming_soon.html")
    
# end def