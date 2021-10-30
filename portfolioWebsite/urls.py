from django.urls import path


from .views import Home, Post, Posts, Profile

urlpatterns = [
    path('', Home, name='home'),
    path('home', Home, name='home'),
    path('post', Post, name='post'),
    path('posts', Posts, name='posts'),
    path('profile', Profile, name='profile'),
    
]