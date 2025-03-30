"""
URL configuration for tts_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from tts_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign-in', views.sign_in, name='sign_in'),
    path('pricing', views.pricing, name='pricing'),
    path('integrations', views.integrations, name='integrations'),
    path('examples', views.examples, name='examples'),
    path("api/speakers/", views.get_speakers, name="get_speakers"),
    path("api/audio/<str:filename>/", views.get_audio, name="get_audio"),
]
