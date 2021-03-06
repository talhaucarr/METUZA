from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import BookForm, BookStoryForm, BookPersonalForm, BookMathForm
from .models import Book, BookStory, BookPersonal, BookMath


# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, "pdf.html", context)

@login_required(login_url="user:login")
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })

@login_required(login_url="user:login")
def upload_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })

@login_required(login_url="user:login")
def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()

    return redirect('book_list')


class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'


class UploadBookView(CreateView):
    model = Book
    # fields = ('title', 'author', 'pdf','cover')
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'

@login_required(login_url="user:login")
def homePage(request):
    return render(request, 'booksHome.html')

@login_required(login_url="user:login")
def story_list(request):
    books = BookStory.objects.all()
    return render(request, 'stroy_list.html', {
        'books': books
    })

@login_required(login_url="user:login")
def upload_story(request):
    if request.method == "POST":
        form = BookStoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stroy_list')
    else:
        form = BookStoryForm
    form = BookStoryForm
    return render(request, 'upload_story.html', {
        'form': form
    })

@login_required(login_url="user:login")
def delete_story(request, pk):
    if request.method == 'POST':
        book = BookStory.objects.get(pk=pk)
        book.delete()

    return redirect('stroy_list')

@login_required(login_url="user:login")
def personal_list(request):
    books = BookPersonal.objects.all()
    return render(request, 'personal_list.html', {
        'books': books
    })

@login_required(login_url="user:login")
def upload_personal(request):
    if request.method == "POST":
        form = BookPersonalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('personal_list')
    else:
        form = BookPersonalForm
    form = BookPersonalForm
    return render(request, 'upload_personal.html', {
        'form': form
    })

@login_required(login_url="user:login")
def delete_personal(request, pk):
    if request.method == 'POST':
        book = BookPersonal.objects.get(pk=pk)
        book.delete()

    return redirect('personal_list')

@login_required(login_url="user:login")
def math_list(request):
    books = BookMath.objects.all()
    return render(request, 'math_list.html', {
        'books': books
    })

@login_required(login_url="user:login")
def upload_math(request):
    if request.method == "POST":
        form = BookMathForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('math_list')
    else:
        form = BookMathForm
    form = BookMathForm
    return render(request, 'upload_math.html', {
        'form': form
    })

@login_required(login_url="user:login")
def delete_math(request, pk):
    if request.method == 'POST':
        book = BookMath.objects.get(pk=pk)
        book.delete()

    return redirect('math_list')
