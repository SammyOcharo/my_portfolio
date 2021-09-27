from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import Home, Post, Posts, Profile

urlpatterns = [
    path('', Home, name='home'),
    path('home', Home, name='home'),
    path('post', Post, name='post'),
    path('posts', Posts, name='posts'),
    path('profile', Profile, name='profile'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)