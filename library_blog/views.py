from django.shortcuts import render
from django.http import HttpResponse
import datetime

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('About me')

def about_pets(request):
    if request.method == 'GET':
        return HttpResponse('Привет, у меня есть котенок')

def system_time(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now().strftime('%I:%M %p'))

