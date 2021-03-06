from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, PostForm, ProfileForm, WorkExperienceForm
from .models import Post, Profile, WorkExperience
from article.models import Article
from article.forms import ArticleForm

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout


def index(request):
    return render(request, "classes.html")


@login_required(login_url="user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id=id)
    if article.author_id == request.user.id:
        form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

        if form.is_valid():
            article = form.save(commit=False)

            print()
            article.author = request.user
            article.save()

            messages.success(request, "Makale Başarıyla Güncellendi.")
            return redirect("/user/profile/{}".format(article.author_id))

        return render(request, "update.html", {"form": form})

    else:
        messages.info(request, "Bu sayfaya erişim hakkınız yok!")
        return render(request, "about.html")


@login_required(login_url="user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id=id)
    if article.author_id == request.user.id:
        article.delete()
        messages.success(request, "Makale Başarıyla Silindi.")
        return redirect("/user/profile/{}".format(article.author_id))
    else:
        messages.info(request, "Bu sayfaya erişim hakkınız yok!")
        return render(request, "about.html")


def showProfile(request, id):
    profile = get_object_or_404(Profile, user_id=id)

    user = get_object_or_404(User, id=id)
    workExperience = WorkExperience.objects.filter(user_id=id)
    articles = Article.objects.filter(author_id=id).order_by('-created_date')
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user

        article.save()

        return redirect("/user/profile/{}".format(id))

    return render(request, "profil.html",
                  {"profile": profile, "user": user, "workExperience": workExperience, "form": form,
                   "articles": articles})


@login_required(login_url="user:login")
def updateProfile(request, id):
    if id == request.user.id:
        profile = get_object_or_404(Profile, user_id=id)
        workExperience = WorkExperience.objects.filter(user_id=id)

        form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
        form2 = WorkExperienceForm(request.POST or None, request.FILES or None)

        if request.method == 'POST' and 'btn1' in request.POST:
            new_profile = form.save(commit=False)

            new_profile.user = request.user

            new_profile.save()
            return redirect("/user/profile/{}".format(id))

        if request.method == 'POST' and 'btn2' in request.POST:
            new_work_experience = form2.save(commit=False)

            new_work_experience.user = request.user

            new_work_experience.save()

            return redirect("/user/profile/{}/dashboard".format(id))

        return render(request, 'updateProfile.html', {"form": form, "form2": form2, "workExperience": workExperience})

    else:
        messages.info(request, "Bu sayfaya erişim hakkınız yok!")
        return render(request, "about.html")


def register(request):
    form = RegisterForm(request.POST or None)

    context = {
        "form": form
    }

    second_form = ProfileForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        profile = second_form.save(commit=False)

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        try:
            newUser = User(username=username, email=email)
            newUser.set_password(password)

            newUser.save()

            login(request, newUser)

            profile.user = request.user
            profile.email = email
            profile.save()
            messages.success(request, "Kayıt Başarılı!")  # info succes falan rengini belirle.

            return redirect("index")

        except:
            messages.warning(request, "Kullanıcı adı başkası tarafından alınmış.")
            return render(request, "register.html", context)

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
