from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


posts =[
    {
        'title' : 'ramu',
        'book' : 'ramayan',
        'time' :'kaliyuga',
    },
{
        'title' : 'krishna',
        'book' : 'bagavat',
        'time' :'dwapar',
    },



]

def home(request):
    return HttpResponse("hoyna ,hoyna my life come closer")


def index(request):
    context ={
        'posts' : posts
    }
    template ='blog/index.html'
    return render(request,template,context)

def detail(request,id):
    post =posts[id]
    context ={
        'post' : post
    }
    template ='blog/detail.html'
    return render(request,template,context)

