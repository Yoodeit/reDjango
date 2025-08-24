#from django.shortcuts import render
import profile

from accountapp.decorators import account_authorized
from accountapp.forms import accountUpdateForm
from accountapp.models import Helloworld
from articleapp.models import Article
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import (HttpResponse, HttpResponseForbidden,
                         HttpResponseRedirect)
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.views.generic.list import MultipleObjectMixin
from profileapp.decorators import profile_authorized
from projectapp.forms import ProjectCreateView
from projectapp.models import Project

# Create your views here.

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateView
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})
    
class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, **kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25