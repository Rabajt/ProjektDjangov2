from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Maintenance mode, please wait until we finish our work :)')

