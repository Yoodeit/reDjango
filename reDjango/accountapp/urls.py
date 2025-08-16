from accountapp.views import accountCreateView, helloworld
from django.urls import include, path

app_name="accountapp"

urlpatterns = [
    path('helloworld/', helloworld, name='helloworld'),
    path('create/', accountCreateView.as_view(),name='create'),
]