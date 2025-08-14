#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def helloworld(request):
    #return HttpResponse('hello')
    return render(request,'base.html')