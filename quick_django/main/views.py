from .models import Book
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    return HttpResponse('こんにちは、世界！')


def temp(request: HttpRequest):
    context = {
        'msg': 'こんにちは、世界！'
    }
    return render(request, 'main/temp.html', context)


def list(request: HttpRequest):
    books = Book.objects.all()
    return render(request, 'main/list.html', {
        'books': books
    })


def rel(request: HttpRequest):
    return render(request, 'main/rel.html', {
        'book': Book.objects.get(pk=1)
    })


def rel2(request: HttpRequest):
    return render(request, 'main/rel2.html', {
        'books': Book.objects.all()
    })
