from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.shortcuts import render

def root(request):
    return HttpResponseRedirect('home_page')

def home_page(request):
    context = {'heading': 'Django Blog'}
    response = render(request, 'index.html', context)
    return HttpResponse(response)
