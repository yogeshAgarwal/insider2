from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.http import HttpResponse
from django.utils.html import escape
# from urlparse import urlparse
from . import methodY
import urllib.request


# from cloudinary.forms import cl_init_js_callbacks
# from .models import Photo
# from .forms import PhotoDirectForm



# Create your views here.
def index(request):
    # print('lol')

    if "GET" == request.method:
        # print(request)
        return render(request, 'assignment/index.html', {})
    else:
        data = request.POST["url"]
        methodY.crop(365,212, data)
        methodY.crop(365,450, data)
        methodY.crop(380,380, data)
        methodY.crop(755,450, data)




        return render(request, 'assignment/index.html', {})


# def crop(width, length, url):
    # http://res.cloudinary.com/ifyogesh/image/upload/w_240,h_200,c_crop/atrpftvogyq1ykwzsdnh.jpg


def first(request):
    return render(request, 'assignment/first.html', {})


# def upload_prompt(request):
#   context = dict(direct_form = PhotoDirectForm())
#   cl_init_js_callbacks(context['direct_form'], request)
#   return render(request, 'upload_prompt.html', context)
