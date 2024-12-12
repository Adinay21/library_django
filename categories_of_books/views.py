from django.shortcuts import render
from . import models

def all_books(request):
    if request.method == 'GET':
        books = models.Book.objects.all().order_by('-id')
        context = {'books': books}
        return render(
            request,
            template_name='tags/all_books.html',
            context=context
        )

def books_for_kids(request):
    if request.method == 'GET':
        kids_books = models.Book.objects.filter(tags__name='Книги для детей').order_by('-id')
        context = {'kids_books': kids_books}
        return render(
            request,
            template_name='tags/books_for_kids.html',
            context=context
        )

def books_for_teens(request):
    if request.method == 'GET':
        teens_books = models.Book.objects.filter(tags__name='Книги для подростков').order_by('-id')
        context = {'teens_books': teens_books}
        return render(
            request,
            template_name='tags/books_for_teens.html',
            context=context
        )

def books_for_youth(request):
    if request.method == 'GET':
        youth_books = models.Book.objects.filter(tags__name='Книги для молодежи').order_by('-id')
        context = {'youth_books': youth_books}
        return render(
            request,
            template_name='tags/books_for_youth.html',
            context=context
        )

def books_for_pensioners(request):
    if request.method == 'GET':
        pensioners_books = models.Book.objects.filter(tags__name='Книги для пенсионеров').order_by('-id')
        context = {'pensioners_books': pensioners_books}
        return render(
            request,
            template_name='tags/books_for_pensioners.html',
            context=context
        )