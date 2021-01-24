from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book

def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not todo.is_favorite
    todo.save()
    return redirect(test)


# def unmark_todo(request, id):
#     todo = ToDo.objects.get(id=id)
#     todo.is_favorite = False
#     todo.save()
#     return redirect(test)

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

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
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


# def close_todo(request, id):
#     todo = ToDo.objects.get(id=id)
#     todo.is_closed = not todo.is_closed
#     todo.save()
#     return redirect(test)

# Create your views here.
