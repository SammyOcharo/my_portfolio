from django.shortcuts import render

# Create your views here.


def Home(request):

    return render(request, 'Home.html')

def Post(request):

    return render(request, 'Post.html')

def Posts(request):

    return render(request, 'Posts.html')

def Profile(request):

    return render(request, 'Profile.html')