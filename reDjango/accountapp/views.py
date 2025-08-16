#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def helloworld(request):
    #return HttpResponse('hello')
    if request.method == "POST":
        return render(request, 'accountapp/helloworld.html', context={'text': 'POST METHOD desu'})
    else:
        return render(request, 'accountapp/helloworld.html', context={'text': 'GET METHOD desu'})