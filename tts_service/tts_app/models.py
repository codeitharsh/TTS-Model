from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# class UserVoice(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     voice_name = models.CharField(max_length=100)
#     audio_sample = models.FileField(upload_to='voice_samples/')

# class GeneratedAudio(models.Model):
#     text = models.TextField()
#     voice = models.ForeignKey(UserVoice, on_delete=models.CASCADE)
#     audio_file = models.FileField(upload_to='generated_audio/')
#     created_at = models.DateTimeField(auto_now_add=True)