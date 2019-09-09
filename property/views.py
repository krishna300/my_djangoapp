from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
def index(request):
    return HttpResponse("I just started my app !!")


def property_list(request):
    property_list =Property.objects.all()
    template ='property/list.html'
    context ={'property_list' :property_list}
    return render(request,template,context)

def property_detail(request,id):
    property_detail =Property.objects.get(id =id)
    template ='property/detail.html'
    context ={'property_detail' :property_detail}
    return render(request,template,context)