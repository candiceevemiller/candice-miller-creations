from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home/index.html')

def projects(request):
    return render(request, 'home/projects.html')

def resume(request):
    return render(request, 'home/resume.html')