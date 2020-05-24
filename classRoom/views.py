from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewClassForm, NewContentForm, NewHomeworkForm, _NewHomeworkDeliveryForm, SecondHomework, \
    ClassPostForm
from django.core.files.storage import FileSystemStorage
from .models import NewClass, ClassContent, ClassHomework, Homework, ClassPost
from django.http import HttpResponseRedirect
from django.contrib import messages

import string
import random
from datetime import datetime, date, time

# Create your views here.

"""def show(request):
    return render(request, "classes.html")"""


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def index(request):
    return render(request, "classes.html")


def show(request):
    # cloud = Cloud.objects.all()
    classes = NewClass.objects.filter(class_teacher_name=request.user)
    context = {
        "classes": classes
    }
    return render(request, "classes.html", context)


@login_required(login_url="user:login")
def addclass(request):
    form = NewClassForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)

        article.class_teacher_name = request.user

        article.save()

        # messages.success(request, "Makale Başarıyla Oluşturuldu.")
        return redirect("index")

    return render(request, "addclasses.html", {"form": form})


def addhomework(request, id):
    classroom = get_object_or_404(NewClass, id=id)
    # print(classroom.id)
    class_content = ClassContent.objects.filter(classroom=id)

    _temp = 0
    temp = id_generator()

    if request.method == "POST":

        for i in class_content:

            form = NewHomeworkForm(request.POST or None)

            if form.is_valid():
                homework = form.save(commit=False)

                homework.class_name = i.class_name
                homework.student_name = i.student_naame
                homework.homework_code = temp
                homework.student_id = i.student_name_id
                homework.classroom_id = id

                if _temp == 0:
                    _form = SecondHomework(request.POST or None)
                    print("sa")

                    tempHomework = _form.save(commit=False)

                    tempHomework.title = form.cleaned_data.get("title")
                    tempHomework.content = form.cleaned_data.get("content")
                    tempHomework.end_date = form.cleaned_data.get("end_date")
                    tempHomework.end_clock = form.cleaned_data.get("end_clock")
                    tempHomework.homework_code = temp
                    tempHomework.classroom_id = id
                    tempHomework.submit_count = 0
                    tempHomework.is_end = 0
                    print("sa")
                    tempHomework.save()
                    _temp = 1

                homework.save()

        return redirect("index")

    else:
        form = NewHomeworkForm()

    return render(request, "addhomework.html", {"classroom": classroom, "form": form})


def classDetail(request, id):
    # classroom = NewClass.objects.filter(id=id).first()
    classroom = get_object_or_404(NewClass, id=id)

    homework = Homework.objects.all()

    post = ClassPost.objects.order_by('-created_date')

    form = ClassPostForm(request.POST or None, request.FILES or None)

    deneme = request.GET.get('kral')

    if deneme:
        print("sa")

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.classroom_id = id
        post.save()

        return redirect("/classes/{}".format(id))

    homework2 = ClassHomework.objects.filter(classroom_id=id).values()

    return render(request, "classDetail.html",
                  {"classroom": classroom, "homework": homework, "id": id, "form": form, "post": post})




def joinClass(request, keyword):
    student = NewContentForm(request.POST or None)

    if keyword:
        articles = NewClass.objects.get(class_name=keyword)

        _student = student.save(commit=False)

        _student.class_name = articles.class_name

        _student.student_naame = request.user

        _student.student_name_id = request.user.id

        _student.classroom_id = articles.id

        _student.save()

        messages.success(request, "Başarıyla Kayıt olundu!")


    else:
        messages.info(request, "Düzgün bir sınıf kodu giriniz.")


def homeworks(request):
    class_content = ClassContent.objects.filter(student_name_id=request.user).values()
    _temp = ""
    _temp2 = ""
    _tempList = list()

    for i in class_content:
        _temp = i['id']
        _tempList.append(i['classroom_id'])
        _temp2 = i['classroom_id']

    homework = ClassHomework.objects.filter(student_id=request.user).order_by('-end_date')
    now = datetime.now()

    zaman = time(int(now.strftime(('%H'))), int(now.strftime(('%M'))), int(now.strftime(('%S'))))

    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime('%Y-%m-%d')

    print("Current Time =", current_time)
    for i in homework:
        print(i)

    # deneme = ClassHomework.objects.filter(student_id=request.user, end_clock__gt=current_time,end_date__gt=current_date).order_by()

    classes = NewClass.objects.filter(id__in=[i for i in _tempList])

    keyword = request.GET.get("deneme")

    if keyword:
        joinClass(request, keyword)

    return render(request, "showHomeworks.html",
                  {"homework": homework, "classes": classes, "class_content": class_content,
                   "current_date": date.today(), "current_time": zaman})


def submitHomework(request, id):
    homework = get_object_or_404(ClassHomework, id=id)
    allHomework = ClassHomework.objects.filter(student_id=request.user)
    if request.method == "POST":
        form = _NewHomeworkDeliveryForm(request.POST, request.FILES, instance=homework)
        if form.is_valid():
            file = form.save(commit=False)
            file.student_id = request.user
            file.is_deliver = 1
            file.save()
            messages.success(request, "Ödev başarıyla teslim edildi.")
            return redirect('/classes/homeworks/')
    else:
        form = _NewHomeworkDeliveryForm()
    form = _NewHomeworkDeliveryForm()
    return render(request, 'submitHomework.html', {
        'form': form, 'homework': homework, 'allHomework': allHomework
    })


def homeworkDetail(request, slug):
    sa = get_object_or_404(Homework, homework_code=slug)
    print(id)
    print(sa.title)
    homeworkss = ClassHomework.objects.filter(homework_code=sa.homework_code)

    return render(request, 'homeworkDetail.html', {'homeworkss': homeworkss, 'sa': sa})


def addPost(request):
    form = ClassPostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.classroom_id = id
        post.save()

        return redirect("index")

def deletePost(request,id):
    post = get_object_or_404(ClassPost, id=id)
    post.delete()
    messages.success(request, "Makale Başarıyla Silindi.")
    return redirect("article:dashboard")