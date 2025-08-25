#from django.shortcuts import render
import profile

from accountapp.decorators import account_authorized
from accountapp.forms import accountUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from profileapp.decorators import profile_authorized
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm # 아까 forms.py서 만든거
    #success_url = reverse_lazy('profileapp:update')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False) # 실제 저장은 안되지만 임시로 저장한다.
        temp_profile.user =  self.request.user
        temp_profile.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

@method_decorator(profile_authorized, 'get')
@method_decorator(profile_authorized, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm # 아까 forms.py서 만든거
    #success_url = reverse_lazy('accountapp:helloworld')
    template_name = 'profileapp/update.html'
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})