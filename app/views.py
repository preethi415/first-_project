from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def guava (request):
    return HttpResponse('pakkakivelli aduko')
def orange(request):
    return HttpResponse('HI HI bye bye')
def mango(request):
    return HttpResponse('<h1><marquee>Asha Dosa Appaadam Vada Rukkuu</marquee></h1>')
def banana(request):
    return HttpResponse('Milkshake') 
