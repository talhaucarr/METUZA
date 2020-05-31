"""met URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from article import views
import folder.views
import ownCloud2.views
import classRoom.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('articles/', include("article.urls")),
    path('user/', include("user.urls")),
    path('classes/', include("classRoom.urls")),
    path('messages/', include("Mesaj.urls")),
    path('forum/', include("forum.urls")),

    path('owncloud/fileUpload/', ownCloud2.views.upload_file, name="upload_file"),
    path('owncloud/fileList/', ownCloud2.views.file_list, name="file_list"),
    path('owncloud/<int:pk>/', ownCloud2.views.delete_file, name="delete_file"),

    path('upload/', folder.views.upload, name="upload"),

    path('books/', folder.views.book_list, name="book_list"),
    path('books/upload/', folder.views.upload_book, name="upload_book"),
    path('books/<int:pk>/', folder.views.delete_book, name="delete_book"),
    path('bookshome/', folder.views.homePage, name='booksHome'),

    path('bookStory/', folder.views.story_list, name="stroy_list"),
    path('bookStory/upload/', folder.views.upload_story, name="upload_story"),
    path('bookStory/<int:pk>/', folder.views.delete_story, name="delete_story"),

    path('bookPersonal/', folder.views.personal_list, name="personal_list"),
    path('bookPersonal/upload/', folder.views.upload_personal, name="upload_personal"),
    path('bookPersonal/<int:pk>/', folder.views.delete_personal, name="delete_personal"),

    path('bookScience/', folder.views.math_list, name="math_list"),
    path('bookScience/upload/', folder.views.upload_math, name="upload_math"),
    path('bookScience/<int:pk>/', folder.views.delete_math, name="delete_math"),

    path('class/books/', folder.views.BookListView.as_view(), name="class_book_list"),
    path('class/books/upload/', folder.views.UploadBookView.as_view(), name="class_upload_book"),

    path('classes/homeworks/<int:id>/submit', classRoom.views.submitHomework, name="submitHomework"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
