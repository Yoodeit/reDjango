from django.urls import path, include
from accountapp.views import helloworld

appname="accountapp"

urlpatterns = [
    path('helloworld/', helloworld, name='helloworld'),
]