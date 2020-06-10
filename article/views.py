from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
from user.models import Profile


# Create your views here.

def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})

    articles = Article.objects.all().order_by("-created_date")
    last_articles = Article.objects.order_by("-created_date")[:5]

    return render(request, "articles.html", {"articles": articles, "last_articles": last_articles})


def index(request):
    last_articles = Article.objects.order_by("-created_date")[:5]
    return render(request, "index.html", {"last_articles": last_articles})


def about(request, id):
    return render(request, "about.html")


@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)  # Sisteme kim giriş yaptıysa onun articlelarını getiriyor

    context = {
        "articles": articles
    }

    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request, "Makale Başarıyla Oluşturuldu.")
        return redirect("index")

    return render(request, "addarticle.html", {"form": form})


def detail(request, id):
    # article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article, id=id)
    profile = get_object_or_404(Profile, user_id=article.author_id)

    return render(request, "detail.html", {"article": article, "profile": profile})


@login_required(login_url="user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if form.is_valid():
        article = form.save(commit=False)

        print()
        article.author = request.user
        article.save()

        messages.success(request, "Makale Başarıyla Güncellendi.")
        return redirect("article:dashboard")

    return render(request, "update.html", {"form": form})


@login_required(login_url="user:login")
def deleteArticle(request, id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request, "Makale Başarıyla Silindi.")
    return redirect("article:dashboard")
