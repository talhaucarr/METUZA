from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")

            newUser = User(username=username, email=email)
            newUser.set_password(password)

            newUser.save()

            login(request, newUser)

            messages.info(request, "Kayit Başarili!")  # info succes falan rengini belirle.

            return redirect("index")
        else:
            form = RegisterForm()

            context = {
                "form": form
            }
            return render(request, "register.html", context)
    else:

        form = RegisterForm()

        context = {
            "form": form
        }

        return render(request, "register.html", context)


def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Kullanıcı Adı veya Parola Hatalı")
            return render(request, "login2-+.html", context)

        messages.success(request, "Başarıyla Giriş Yapıldı")

        login(request, user)
        return redirect("index")

    return render(request, "login2.html", context)


def logoutUser(request):
    logout(request)
    messages.success(request, "Başarıyla Çıkış Yapıldı")
    return redirect("index")
