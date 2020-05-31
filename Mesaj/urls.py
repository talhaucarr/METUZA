from django.contrib import admin
from django.urls import path
from . import views

app_name = "messages"

urlpatterns = [
    path('', views.msgHome, name="msgHome"),
    path('sentMessage', views.sendMessage, name="sendMessage"),
    path('inbox', views.inBox, name="inBox"),
    path('sentbox', views.sentBox, name="sentBox"),

]

