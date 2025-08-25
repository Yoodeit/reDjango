
from django.urls import path
from projectapp.views import (ProjectCreateView, ProjectDetailView,
                              ProjectListView)
from subscribeapp.views import SubscriptionListView, SubscriptionView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list'),
    
]