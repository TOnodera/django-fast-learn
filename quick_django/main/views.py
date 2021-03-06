from .forms import BookForm
from .models import Book
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_POST


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


def form_input(request: HttpRequest):
    form = BookForm()
    return render(request, 'main/form_input.html', {
        'form': form
    })


@require_POST
def form_process(request: HttpRequest):
    form = BookForm(request.POST)
    if form.is_valid():
        return render(request, 'main/form_process.html', {
            'form': form
        })
    else:
        return render(request, 'main/form_input.html', {
            'form': form
        })
