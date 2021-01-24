from django.shortcuts import render, HttpResponse
from .models import ToDo, Book

def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})


def books(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})

def add_book(request):
    form = request.POST
    book = Book(
        title=form["title"],
        subtitle=form["subtitle"],
        description=form["description"],
        price=form["price"],
        genre=["genre"],
        author=["author"],
        year=form["date"][:10]
    )

    book.save()

    return redirect(books)


def second(request):
    return HttpResponse("test 2 page")


def third(request):
    return HttpResponse("This is page test3")

def lesson1(request):
    return render(request, "lesson1.html")

def lesson2(request):
    return render(request, "lesson2.html")

def lesson3(request):
    return render(request, "lesson3.html")




# Create your views here.
