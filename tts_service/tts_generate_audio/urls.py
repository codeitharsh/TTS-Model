
from django.urls import path
from tts_generate_audio import views

urlpatterns = [
    path('/generate_speech', views.GenerateSpeechView.as_view() , name='generate_speech'),
]
