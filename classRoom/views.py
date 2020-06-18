from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewClassForm, NewContentForm, NewHomeworkForm, _NewHomeworkDeliveryForm, SecondHomework, \
    ClassPostForm, NoteForm
from django.core.files.storage import FileSystemStorage
from .models import NewClass, ClassContent, ClassHomework, Homework, ClassPost
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib.auth.models import User

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


@login_required(login_url="user:login")
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


@login_required(login_url="user:login")
def addhomework(request, id):
    classroom = get_object_or_404(NewClass, id=id)
    temp_email = list()

    if classroom.class_teacher_name_id == request.user.id:
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

                    temp_email2 = get_object_or_404(User, id=i.student_name_id)
                    temp_email.append(temp_email2.email)

                    if _temp == 0:
                        _form = SecondHomework(request.POST or None)

                        tempHomework = _form.save(commit=False)

                        tempHomework.title = form.cleaned_data.get("title")
                        tempHomework.content = form.cleaned_data.get("content")
                        tempHomework.end_date = form.cleaned_data.get("end_date")
                        tempHomework.end_clock = form.cleaned_data.get("end_clock")
                        tempHomework.homework_code = temp
                        tempHomework.classroom_id = id
                        tempHomework.submit_count = 0
                        tempHomework.is_end = 0
                        tempHomework.save()
                        _temp = 1

                    homework.save()



                text_content = 'METUZA - Bilgilendirme'
                html_content = '<p>Yeni bir  <strong>ödeviniz</strong> var.</p>'
                msg = EmailMultiAlternatives("Ödev", text_content, settings.EMAIL_HOST_USER, [i for i in temp_email])
                msg.attach_alternative(html_content,"text/html")
                msg.send()

            return redirect("index")

        else:
            form = NewHomeworkForm()

        return render(request, "addhomework.html", {"classroom": classroom, "form": form})

    else:
        messages.info(request, "Bu sayfaya erişim hakkınız yok!")
        return render(request, "about.html")


@login_required(login_url="user:login")
def classDetail(request, id):
    # classroom = NewClass.objects.filter(id=id).first()
    classroom = get_object_or_404(NewClass, id=id)
    print(request.user.id)

    if classroom.class_teacher_name_id == request.user.id:

        homework = Homework.objects.all()

        post = ClassPost.objects.order_by('-created_date')

        form = ClassPostForm(request.POST or None, request.FILES or None)

        deneme = request.GET.get('kral')

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.classroom_id = id
            post.save()

            return redirect("/classes/{}".format(id))

        homework2 = ClassHomework.objects.filter(classroom_id=id).values()

        return render(request, "classDetail.html",
                      {"classroom": classroom, "homework": homework, "id": id, "form": form, "post": post})

    else:
        messages.info(request, "Bu sayfaya erişiminiz yok!")
        return render(request, "about.html")


@login_required(login_url="user:login")
def joinClass(request, keyword, homework, class_content, classes, zaman):
    student = NewContentForm(data=request.POST)

    if student.is_valid():

        if keyword:

            articles = NewClass.objects.get(class_name=keyword)

            _student = student.save(commit=False)

            _student.class_name = articles.class_name

            _student.student_naame = request.user

            _student.student_name_id = request.user.id

            _student.classroom_id = articles.id

            _student.save()

            className = ClassContent.objects.filter(class_name=keyword)
            if not className:
                return render(request, "showHomeworks.html",
                              {"homework": homework, "classes": classes, "class_content": class_content,
                               "current_date": date.today(), "current_time": zaman})
            else:
                homeworkss = Homework.objects.filter(classroom_id=className[0].classroom_id)

                for i in homeworkss:
                    form = ClassHomework(end_clock=i.end_clock, end_date=i.end_date,
                                         title=i.title, content=i.content, class_name=keyword,
                                         student_name=request.user.username, homework_code=i.homework_code,
                                         student_id=request.user.id, classroom_id=i.classroom_id)
                    form.save()

                messages.success(request, "Başarıyla Kayıt olundu!")

                return render(request, "showHomeworks.html",
                              {"homework": homework, "classes": classes, "class_content": class_content,
                               "current_date": date.today(), "current_time": zaman})

        else:
            messages.info(request, "Düzgün bir sınıf kodu giriniz.")


@login_required(login_url="user:login")
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

    classes = NewClass.objects.filter(id__in=[i for i in _tempList])

    keyword = request.POST.get("deneme")

    if request.POST:
        if keyword:
            try:
                joinClass(request, keyword, homework, class_content, classes, zaman)
                return render(request, "showHomeworks.html",
                              {"homework": homework, "classes": classes, "class_content": class_content,
                               "current_date": date.today(), "current_time": zaman})
            except:
                messages.warning(request, "Lütfen geçerli bir kod giriniz.")

    return render(request, "showHomeworks.html",
                  {"homework": homework, "classes": classes, "class_content": class_content,
                   "current_date": date.today(), "current_time": zaman})


@login_required(login_url="user:login")
def studentClass(request, id):
    class_content = ClassContent.objects.filter(student_name_id=request.user).values()
    temp = get_object_or_404(NewClass, id=id)
    _temp = ""
    _temp2 = ""
    _tempList = list()

    for i in class_content:
        _temp = i['id']
        _tempList.append(i['classroom_id'])
        _temp2 = i['classroom_id']

    homework = ClassHomework.objects.filter(student_id=request.user, classroom_id=id).order_by('-end_date')
    now = datetime.now()

    zaman = time(int(now.strftime(('%H'))), int(now.strftime(('%M'))), int(now.strftime(('%S'))))

    classes = NewClass.objects.filter(id__in=[i for i in _tempList])

    keyword = request.GET.get("deneme")

    """if request.POST:

        if keyword:
            try:
                joinClass(request, keyword)
            except:
                messages.warning(request, "Lütfen geçerli bir kod giriniz.")"""

    return render(request, "studentClass.html",
                  {"homework": homework, "classes": classes, "class_content": class_content,
                   "current_date": date.today(), "current_time": zaman, "temp": temp})


@login_required(login_url="user:login")
def submitHomework(request, id):
    now = datetime.now()

    zaman = time(int(now.strftime(('%H'))), int(now.strftime(('%M'))), int(now.strftime(('%S'))))
    homework = get_object_or_404(ClassHomework, id=id)

    if homework.student_name == request.user.username:

        if (homework.end_date > date.today()) or ((homework.end_date == date.today()) and homework.end_clock > zaman):

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

        else:
            messages.warning(request, "Ödevin süresi geçmiş. Bu ödevi teslim edemezsiniz!")
            return render(request, "about.html")

    else:
        messages.info(request, "Bu ödeve erişim hakkınız yok!")
        return render(request, "about.html")


@login_required(login_url="user:login")
def homeworkDetail(request, slug):
    sa = get_object_or_404(Homework, homework_code=slug)
    homeworkss = ClassHomework.objects.filter(homework_code=sa.homework_code)

    if request.GET.get("deneme41"):
        print(request.GET.get("sa"))

    return render(request, 'homeworkDetail.html', {'homeworkss': homeworkss, 'sa': sa})


@login_required(login_url="user:login")
def dashboard(request, id):
    classroom = get_object_or_404(NewClass, id=id)

    if classroom.class_teacher_name_id == request.user.id:

        code = classroom.class_code

        class_content = ClassContent.objects.filter(classroom_id=id)

        homeworks = Homework.objects.filter(classroom_id=id)

        posts = ClassPost.objects.filter(classroom_id=id)

        return render(request, "classDashboard.html",
                      {"classroom": classroom, "class_content": class_content, "posts": posts, "code": code,
                       "homeworks": homeworks})

    else:
        messages.info(request, "Bu sayfaya erişim izniniz yok!")
        return render(request, "about.html")


@login_required(login_url="user:login")
def addPost(request):
    form = ClassPostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.classroom_id = id
        post.save()

        return redirect("index")


@login_required(login_url="user:login")
def updatePost(request, id):
    post = get_object_or_404(ClassPost, id=id)
    if post.author_id == request.user.id:
        form = ClassPostForm(request.POST or None, request.FILES or None, instance=post)

        if form.is_valid():
            article = form.save(commit=False)

            article.author = request.user
            article.save()

            messages.success(request, "Makale Başarıyla Güncellendi.")
            return redirect("/classes/{}/dashboard".format(post.classroom_id))

        return render(request, "update_post.html", {"form": form})

    else:
        messages.info(request, "Bu sayfaya erişim hakkınız yok!")
        return render(request, "about.html")


def updateHomework(request, slug):
    pass


@login_required(login_url="user:login")
def deletePost(request, id):
    post = get_object_or_404(ClassPost, id=id)
    if post.author_id == request.user.id:

        post.delete()
        messages.success(request, "Gönderi Başarıyla Silindi.")
        return redirect("/classes/{}/dashboard".format(post.classroom_id))
    else:
        messages.info(request, "Bu sayfaya erişim hakkınız yok!")
        return render(request, "about.html")


@login_required(login_url="user:login")
def deleteHomework(request, slug):
    classroom = get_object_or_404(Homework, homework_code=slug)
    ClassHomework.objects.filter(homework_code=slug).delete()
    Homework.objects.filter(homework_code=slug).delete()
    messages.success(request, "ödev Başarıyla Silindi.")
    return redirect("/classes/{}/dashboard".format(classroom.classroom_id))
