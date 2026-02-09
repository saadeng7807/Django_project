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
    return render(request,'index.html')

# def depts(request):
#      return render(request,'depts.html')


def depts(request):

    departments=[
        "الموارد البشرية",
        "المحاسبة",
        "تقنية المعلومات",
        "قسم المشتريات"
    ]

    s="SAAD SALEM"
    tax="2500"
    template=loader.get_template('depts.html')
    
    context={
        'depts':departments,
        's1':s,
        't':tax
    }

    return HttpResponse(template.render(context,request))






