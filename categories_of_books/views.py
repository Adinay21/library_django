from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache




from django.shortcuts import render
from . import models
from django.views import generic
from categories_of_books.models import Book


@method_decorator(cache_page(60 * 15), name='dispatch')
class AllBooksView(generic.ListView):
    template_name = 'tags/all_books.html'
    context_object_name = 'books'
    model = Book

    def get_queryset(self):
        alls = cache.get('alls')
        if not alls:
            alls = self.model.objects.all().order_by('-id')
            cache.set('alls', alls, 60 * 15)
        return alls

# def all_books(request):
#     if request.method == 'GET':
#         books = models.Book.objects.all().order_by('-id')
#         context = {'books': books}
#         return render(
#             request,
#             template_name='tags/all_books.html',
#             context=context
#         )

@method_decorator(cache_page(60 * 15), name='dispatch')
class BooksForKidsView(generic.ListView):
    template_name = 'tags/books_for_kids.html'
    context_object_name = 'kids_books'
    model = Book

    def get_queryset(self):
        kids = cache.get('kids')
        if not kids:
            kids = self.model.objects.filter(tags__name='Книги для детей').order_by('-id')
            cache.set('kids', kids, 60 * 15)
        return kids

# def books_for_kids(request):
#     if request.method == 'GET':
#         kids_books = models.Book.objects.filter(tags__name='Книги для детей').order_by('-id')
#         context = {'kids_books': kids_books}
#         return render(
#             request,
#             template_name='tags/books_for_kids.html',
#             context=context
#         )

@method_decorator(cache_page(60 * 15), name='dispatch')
class BooksForTeensView(generic.ListView):
    template_name = 'tags/books_for_teens.html'
    context_object_name = 'teens_books'
    model = Book

    def get_queryset(self):
        teens = cache.get('teens')
        if not teens:
            teens = self.model.objects.filter(tags__name='Книги для подростков').order_by('-id')
            cache.set('teens', teens, 60 * 15)
        return teens

# def books_for_teens(request):
#     if request.method == 'GET':
#         teens_books = models.Book.objects.filter(tags__name='Книги для подростков').order_by('-id')
#         context = {'teens_books': teens_books}
#         return render(
#             request,
#             template_name='tags/books_for_teens.html',
#             context=context
#         )

@method_decorator(cache_page(60 * 15), name='dispatch')
class BooksForYouthView(generic.ListView):
    template_name = 'tags/books_for_youth.html'
    context_object_name = 'youth_books'
    model = Book

    def get_queryset(self):
        youth = cache.get('youth')
        if not youth:
            youth = self.model.objects.filter(tags__name='Книги для молодежи').order_by('-id')
            cache.set('youth', youth, 60 * 15)
        return youth

# def books_for_youth(request):
#     if request.method == 'GET':
#         youth_books = models.Book.objects.filter(tags__name='Книги для молодежи').order_by('-id')
#         context = {'youth_books': youth_books}
#         return render(
#             request,
#             template_name='tags/books_for_youth.html',
#             context=context
#         )

@method_decorator(cache_page(60 * 15), name='dispatch')
class BooksForPensionersView(generic.ListView):
    template_name = 'tags/books_for_pensioners.html'
    context_object_name = 'pensioners_books'
    model = Book

    def get_queryset(self):
        pensioners = cache.get('pensioners')
        if not pensioners:
            pensioners = self.model.objects.filter(tags__name='Книги для пенсионеров').order_by('-id')
            cache.set('pensioners', pensioners, 60 * 15)
        return pensioners

# def books_for_pensioners(request):
#     if request.method == 'GET':
#         pensioners_books = models.Book.objects.filter(tags__name='Книги для пенсионеров').order_by('-id')
#         context = {'pensioners_books': pensioners_books}
#         return render(
#             request,
#             template_name='tags/books_for_pensioners.html',
#             context=context
#         )

def clear_basket_cache(sender, **kwargs):
    cache.delete('alls')
    cache.delete('kids')
    cache.delete('teens')
    cache.delete('youth')
    cache.delete('pensioners')