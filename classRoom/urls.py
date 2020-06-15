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
    path('<int:id>/dashboard', views.dashboard, name="dashboard"),
    path('dashboard/<int:id>/delete', views.deletePost, name="deletePost"),
    path('dashboard/<int:id>/update', views.updatePost, name="updatePost"),
    path('dashboard/<slug:slug>/delete', views.deleteHomework, name="deleteHomework"),
    path('<slug:slug>/homeworkDetail', views.homeworkDetail, name="homeworkDetail"),
    path('homeworks/', views.homeworks, name="homeworks"),
    path('homeworks/<int:id>', views.studentClass, name="studentClass"),
]
