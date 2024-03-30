from django.shortcuts import render
from .models import Book

# Create your views here.

def index (request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "books": books
    })

def book_detail(request, id):
    return render(request, "book_outlet/book_detail.html" )