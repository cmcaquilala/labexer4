from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    books = Book.objects.all()
    authors = Author.objects.all()

    data = {"books" : books,
            "authors" : authors,}
    return render(request, 'book_crud/home.html', data)

def add_book(request):
    form = BookForm()

    if(request.method == 'POST'):
        form = BookForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/")

    data = {"form" : form}
    return render(request, 'book_crud/add_book.html', data)

def edit_book(request,pk):
    book = Book.objects.get(id=pk)
    form = BookForm(instance=book)

    if(request.method == 'POST'):
        form = BookForm(request.POST,instance=book)
        if(form.is_valid()):
            form.save()
            return redirect("/")

    data = {"book" : book, "form" : form}
    return render(request, 'book_crud/edit_book.html', data)

def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect("/")

def add_author(request):
    form = AuthorForm()

    if(request.method == 'POST'):
        form = AuthorForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("/")

    data = {"form" : form}
    return render(request, 'book_crud/add_author.html', data)

def edit_author(request, pk):
    author = Author.objects.get(id=pk)
    form = AuthorForm(instance=author)

    if(request.method == 'POST'):
        form = AuthorForm(request.POST, instance=author)
        if(form.is_valid()):
            form.save()
            return redirect("/")

    data = {"author" : author, "form" : form}
    return render(request, 'book_crud/edit_author.html', data)

def delete_author(request, pk):
    author = Author.objects.get(id=pk)
    author.delete()
    return redirect("/")