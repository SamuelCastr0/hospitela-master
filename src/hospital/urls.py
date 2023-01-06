from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, reverse

def redirect_request_to_index(request):
    ''' SEND THE USER TO THE INDEX PAGE IF THE REQUESTED URL DOES NOT EXIST'''
    return redirect('index')


urlpatterns = [
    path('protected/', include([
        path('admin/', admin.site.urls),
    ])),
    path('', include('screening.urls')),
    path('', include('users.urls')),
    path('', redirect_request_to_index),
]
