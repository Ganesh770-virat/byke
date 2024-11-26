from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def re(request):
    return HttpResponse('<h1>red enfield is my favourite</h1>')
