from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from django.contrib import messages
from .models import Article, Comment
from classRoom.models import ClassHomework, ClassContent, NewClass
from user.models import Profile

from datetime import datetime, date, time


# Create your views here.

def addComment(request, id):
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author, comment_content=comment_content)

        newComment.article = article

        newComment.save()

    return redirect("/articles/article/" + str(id))


def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request, "articles.html", {"articles": articles})

    articles = Article.objects.all().order_by("-created_date")
    last_articles = Article.objects.order_by("-created_date")[:5]

    return render(request, "articles.html", {"articles": articles, "last_articles": last_articles})


def index(request):
    now = datetime.now()

    zaman = time(int(now.strftime(('%H'))), int(now.strftime(('%M'))), int(now.strftime(('%S'))))

    last_articles = Article.objects.order_by("-created_date")[:5]
    if request.user.is_authenticated:
        allHomework = ClassHomework.objects.filter(student_id=request.user)

        class_content = ClassContent.objects.filter(student_name_id=request.user).values()
        _temp = ""
        _temp2 = ""
        _tempList = list()

        for i in class_content:
            _temp = i['id']
            _tempList.append(i['classroom_id'])
            _temp2 = i['classroom_id']

        classes = NewClass.objects.filter(id__in=[i for i in _tempList])

        return render(request, "index.html",
                      {"last_articles": last_articles, "allHomework": allHomework, "classes": classes,
                       "current_date": date.today(),
                       "current_time": zaman})

    return render(request, "index.html",
                  {"last_articles": last_articles, "current_date": date.today(),
                   "current_time": zaman})


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

    article = get_object_or_404(Article, id=id)
    profile = get_object_or_404(Profile, user_id=article.author_id)
    comments = Comment.objects.filter(article_id = id)

    return render(request, "detail.html", {"article": article, "profile": profile, "comments": comments})


@login_required(login_url="user:login")
def updateArticle(request, id):
    article = get_object_or_404(Article, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if form.is_valid():
        article = form.save(commit=False)

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
