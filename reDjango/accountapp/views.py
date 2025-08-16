#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import Helloworld

# Create your views here.

def helloworld(request):
    #return HttpResponse('hello')
    if request.method == "POST":

        temp = request.POST.get('helloworld_input')

        new_helloworld = Helloworld();
        new_helloworld.text = temp
        new_helloworld.save()
        
        return render(request, 'accountapp/helloworld.html', context={'helloworld_output': new_helloworld})
    else:
        return render(request, 'accountapp/helloworld.html', context={'text': 'GET METHOD desu'})