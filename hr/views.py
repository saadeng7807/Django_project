from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def welcome(request):
    return HttpResponse('Welcome To First Lesson in Views :)')


def total(request):
    return HttpResponse('1000')

def tax(request,number):
   return HttpResponse(number*0.15)

def landpage(request):
    return HttpResponse('Welcome to Home Page ')

def show_index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def depts(request):
    template=loader.get_template('depts.html')
    return HttpResponse(template.render())



