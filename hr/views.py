from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return HttpResponse('Welcome To First Lesson in Views :)')


def total(request):
    return HttpResponse('1000')

def tax(request,number):
   return HttpResponse(number*0.15)

def landpage(request):
    return HttpResponse('Welcome to Home Page ')



