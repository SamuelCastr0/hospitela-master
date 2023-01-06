from django.urls import path, include

from . import views

urlpatterns = [
    path('protected/', include([
        path('users/', include([
            path('login/', views.LoginView.as_view(), name='login'),
            path('register-user/', views.RegisterUserView.as_view(), name='register-user'),
        ])),
    ])),
    path('users/', include([
        path('logout/', views.LogoutView.as_view(), name='logout'),
    ])),
]
