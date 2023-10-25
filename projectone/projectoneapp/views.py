from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return  HttpResponse('Hello world')
    # value pass ..concate with value in home.html
    name = 'arithmetic operations'
    return render(request, "home.html", {'obj': name})


def oprn(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    z = x + y
    a = x - y
    b = x * y
    c = x / y
    return render(request, "result.html", {'add':z, 'sub': a, 'mul': b, 'div': c})
