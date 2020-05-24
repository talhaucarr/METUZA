from django.contrib import admin
from django.urls import path
from classRoom import views

app_name = "classRoom"

urlpatterns = [

    path('', views.show, name="classes"),
    path('addclasses/', views.addclass, name="addclass"),
    path('<int:id>/addhomework', views.addhomework, name="addhomework"),
    path('joinclass/', views.joinClass, name="joinclass"),
    path('<int:id>/', views.classDetail, name="classDetail"),
    path('<slug:slug>/homeworkDetail', views.homeworkDetail, name="homeworkDetail"),
    path('homeworks/', views.homeworks, name="homeworks"),
]
