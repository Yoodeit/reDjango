#from django.shortcuts import render
from accountapp.models import Helloworld
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

# Create your views here.

def helloworld(request):
    #return HttpResponse('hello')
    if request.method == "POST":

        temp = request.POST.get('helloworld_input')

        new_helloworld = Helloworld();
        new_helloworld.text = temp
        new_helloworld.save()

        #helloworld_list = Helloworld.objects.all();
        return HttpResponseRedirect(reverse('accountapp:helloworld'))
        
        #return render(request, 'accountapp/helloworld.html', context={'helloworld_list': helloworld_list})
    else:
        helloworld_list = Helloworld.objects.all();
        return render(request, 'accountapp/helloworld.html', context={'helloworld_list': helloworld_list})
    
class accountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:helloworld')
    # 함수와 클래스가 파이썬에서 불러와지는 방식의 차이 때문에 클래스에서는 reverse_lazy를 써야 함. 기능은 똑같음
    template_name = 'accountapp/create.html'