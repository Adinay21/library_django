from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from . import models



def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.BookModel, id=id)
        context = {
            'book_id': book_id,
        }
        return render(request, 'book_detail.html', context=context)


def book_list_view(request):
    if request.method == 'GET':
        book_list = models.BookModel.objects.all().order_by('-id')
        context = {
            'book_list': book_list,
        }
        return render(request, 'book.html', context)

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('About me')

def about_pets(request):
    if request.method == 'GET':
        return HttpResponse('Привет, у меня есть котенок')

def system_time(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now().strftime('%I:%M %p'))

