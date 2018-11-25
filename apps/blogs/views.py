# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = 'placeholder to later display all the list of blogs'
    return HttpResponse(response)

def new(request):
    response = 'placeholder to display a new form to create a new blog'
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request, number):
    response = 'placeholder to display blog {}'.format(number)
    return HttpResponse(response)

def edit(request, number):
    response = 'placeholder to edit blog {}'.format(number)
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/blogs')