
from django.urls import path
from tts_generate_audio import views

urlpatterns = [
    path('/generate_speech', views.generate_speech , name='generate_speech'),
]
