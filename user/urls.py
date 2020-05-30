from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/<int:id>', views.showProfile, name="showProfile"),
    path('profile/<int:id>/dashboard/', views.updateProfile, name="updateProfile"),
    path('dashboard/update/<int:id>', views.updateArticle, name="updateArticle"),
    path('dashboard/delete/<int:id>', views.deleteArticle, name="deleteArticle")

]
