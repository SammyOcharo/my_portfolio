from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Project, Feedback

# Create your views here.


def Home(request):

    feedbacks_list = Feedback.objects.all().order_by('-id')
    paginator = Paginator(feedbacks_list, 3)
    page_number = request.GET.get('page')
    try:
        feedbacks = paginator.page(page_number)
    except PageNotAnInteger:
        feedbacks = paginator.page(1)
    context = {
        'feedbacks': feedbacks
    }

    return render(request, 'Home.html', context)

def Post(request):
    
    return render(request, 'Post.html')

def Posts(request):
    posts = Project.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'Posts.html', context)

def Profile(request):

    return render(request, 'Profile.html')