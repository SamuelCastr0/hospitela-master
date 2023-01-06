from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import HospitalUser


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        try:
            email = request.POST['email']
            password = request.POST['password']
            username = HospitalUser.objects.get(email=email)

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('index')
        except:
            return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class RegisterUserView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'users/register-user.html')
        else:
            redirect('login')

    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        occupation = int(request.POST['occupation'])

        passwd_is_valid = RegisterUserView.is_password_valid(password, confirm_password)
        user_does_not_exists = not RegisterUserView.is_user_already_registered(name, email)

        if passwd_is_valid and user_does_not_exists:
            user = HospitalUser.objects.create_user(username=name, email=email, password=password)
            user.set_user_occupation(occupation)
            user.save()
            return redirect('index')
        return redirect('login')

    @classmethod
    def is_password_valid(cls, password1, password2):
        if password1.strip() == password2.strip():
            return True
        return False

    @classmethod
    def is_user_already_registered(cls, name, email):
        try:
            user_with_name = HospitalUser.objects.get(username=name)
            user_with_email = HospitalUser.objects.get(email=email)
        except:
            user_with_name = False
            user_with_email = False

        if user_with_name or user_with_email:
            return True
        return False
