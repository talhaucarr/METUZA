from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from user.models import Profile
from .forms import MsgForm
from .models import Msg


# Create your views here.

def index(request):
    return render(request, "classes.html")


def msgHome(request):
    form = MsgForm(request.POST or None, request.FILES or None)
    profile = get_object_or_404(Profile, user_id=request.user)

    return render(request, "msgHome.html", {"form": form, "profile": profile})


def sendMessage(request):
    form = MsgForm(request.POST or None, request.FILES or None)
    profile = get_object_or_404(Profile, user_id=request.user)
    user = User.objects.all()

    if form.is_valid():
        msg = form.save(commit=False)

        msg.sender = request.user

        for i in user:
            if i.username == msg.username:
                print(i.pk)
                msg.reciever_id = i.id

                msg.save()

                return redirect("/messages")

        messages.info(request, "Hatalı kullanıcı adı!")

    return render(request, "Message.html", {"form": form, "profile": profile})


def inBox(request):
    messages = Msg.objects.filter(reciever=request.user)
    print("in")
    profile = get_object_or_404(Profile, user_id=request.user)
    return render(request, "inbox.html", {"messages": messages, "profile": profile})


def sentBox(request):
    messagess = Msg.objects.filter(sender=request.user).order_by("-created_at")
    print("sent")
    profile = get_object_or_404(Profile, user_id=request.user)
    profiles = Profile.objects.all()
    return render(request, "sentbox.html", {"messagess": messagess, "profile": profile, "profiles": profiles})
