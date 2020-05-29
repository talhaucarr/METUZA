from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RegisterForm, LoginForm, PostForm, ProfileForm, WorkExperienceForm
from .models import Post, Profile, WorkExperience
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def index(request):
    return render(request, "classes.html")


def showProfile(request, id):
    profile = get_object_or_404(Profile, user_id=5)
    user = get_object_or_404(User, id=5)

    return render(request, "profil.html", {"profile": profile, "user": user})


def updateProfile(request,id):
    profile = get_object_or_404(Profile, user_id=id)

    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        new_profile = form.save(commit=False)

        new_profile.user = request.user

        profile.save()
        return redirect("/user/profile/{}".format(id))

    return render(request, 'updateProfile.html', {"form": form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        second_form = ProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            profile = second_form.save(commit=False)

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            email = form.cleaned_data.get("email")

            newUser = User(username=username, email=email)
            newUser.set_password(password)

            newUser.save()

            login(request, newUser)

            profile.user = request.user
            profile.email = email
            profile.save()
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
