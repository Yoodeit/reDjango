#from django.shortcuts import render
from accountapp.decorators import account_authorized
from accountapp.forms import accountUpdateForm
from articleapp.models import Article
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.views.generic.list import MultipleObjectMixin

has_ownership = [login_required, account_authorized]
# Create your views here.
    
class accountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:helloworld')
    # 함수와 클래스가 파이썬에서 불러와지는 방식의 차이 때문에 클래스에서는 reverse_lazy를 써야 함. 기능은 똑같음
    template_name = 'accountapp/create.html'
        

class accountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(accountDetailView, self).get_context_data(object_list = object_list, **kwargs)
    
    


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class accountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = accountUpdateForm
    success_url = reverse_lazy('accountapp:helloworld')
    # 함수와 클래스가 파이썬에서 불러와지는 방식의 차이 때문에 클래스에서는 reverse_lazy를 써야 함. 기능은 똑같음
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class accountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'