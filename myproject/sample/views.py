from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add(request):
    a=request.GET.get('a',10)
    b=request.GET.get('b',10)
    c=int(a)+int(b)
    return HttpResponse(f"The addition of {a},{b} is {c}")
def sub(request):
    a=request.GET.get('a',10)
    b=request.GET.get('b',10)
    c=int(a)-int(b)
    
    return HttpResponse(f"The substraction of {a},{b} is {c}")
def mul(request):
    a=request.GET.get('a',10)
    b=request.GET.get('b',10)
    c=int(a)*int(b)
    return HttpResponse(f"The multiplication of {a},{b} is {c}")
def div(request):
    a=request.GET.get('a',10)
    b=request.GET.get('b',10)
    c=int(a)/int(b)
    return HttpResponse(f"The division of {a},{b} is {c}")
