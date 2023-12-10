
from django.contrib import admin
from django.urls import path,include
from website.views import welcome
urlpatterns = [
    path('admin/', admin.site.urls),
    path(' /' , welcome),
    path('nevigation/', include('nevigation.urls'))
]
