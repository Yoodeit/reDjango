#from django.shortcuts import render
from accountapp.forms import accountUpdateForm
from accountapp.models import Helloworld
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

# Create your views here.

def helloworld(request):
    #return HttpResponse('hello')

    if request.user.is_authenticated:

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
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))
    
class accountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:helloworld')
    # 함수와 클래스가 파이썬에서 불러와지는 방식의 차이 때문에 클래스에서는 reverse_lazy를 써야 함. 기능은 똑같음
    template_name = 'accountapp/create.html'
        

class accountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class accountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = accountUpdateForm
    success_url = reverse_lazy('accountapp:helloworld')
    # 함수와 클래스가 파이썬에서 불러와지는 방식의 차이 때문에 클래스에서는 reverse_lazy를 써야 함. 기능은 똑같음
    template_name = 'accountapp/update.html'
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
             return super().get(*args, **kwargs)
        else:
             return HttpResponseForbidden()
        
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()

class accountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
             return super().get(*args, **kwargs)
        else:
             return HttpResponseForbidden()
        
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()