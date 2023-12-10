from django.urls import path
# from login.views import loginHome
from .import views

urlpatterns = [
    # path('', loginHome , name= 'home',)
     path('', views.loginHome , name = 'home'),
     path('Bform/', views.Bform, name= "form"),
     path('Dform/', views.Dform , name = 'D_form')
]
