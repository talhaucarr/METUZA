from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from django.core.files.storage import FileSystemStorage

from django.views.generic import ListView, CreateView

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

from .forms import CloudForm
from .models import Cloud


@login_required(login_url="user:login")
def file_list(request):
    # cloud = Cloud.objects.all()
    cloud = Cloud.objects.filter(authorr=request.user)
    return render(request, "file_list.html", {
        'cloud': cloud
    })


def upload_file(request):
    if request.method == "POST":
        form = CloudForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)

            file.authorr = request.user

            file.save()
            return redirect('file_list')
    else:
        form = CloudForm()
    form = CloudForm()
    return render(request, 'upload_file.html', {
        'form': form
    })


def delete_file(request, pk):
    if request.method == 'POST':
        book = Cloud.objects.get(pk=pk)
        book.delete()

    return redirect('file_list')

# Create your views here.
