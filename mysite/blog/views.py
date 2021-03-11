from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'RyanT',
        'title': 'Blog 1',
        'content': 'Dummy Post',
        'date_posted': '11th March, 2021'
    },
    {
        'author': 'RyanT',
        'title': 'Blog 2',
        'content': 'Dummy Post2',
        'date_posted': '11th March, 2021'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)