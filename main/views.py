from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, "index.html")


def test(request):
    return render(request, "test.html")


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
