from django.urls import path
from nevigation.views import welcome
urlpatterns = [
    path(' ', welcome)
]
