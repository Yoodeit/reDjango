from accountapp.views import accountCreateView, helloworld
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

app_name="accountapp"

urlpatterns = [
    path('helloworld/', helloworld, name='helloworld'),
    path('login/', LoginView.as_view(template_name = 'accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page="accountapp:helloworld"), name='logout'),
    path('create/', accountCreateView.as_view(),name='create'),
]