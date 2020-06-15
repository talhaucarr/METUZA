from django.db import models
from ckeditor.fields import RichTextField
import datetime
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# Create your models here.
class NewClass(models.Model):
    class_name = models.CharField(max_length=20, verbose_name="Sınıf Adı:")
    class_teacher_name = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yükleyen")
    class_code = models.CharField(max_length=6, default=id_generator)


class ClassContent(models.Model):
    classroom = models.ForeignKey(NewClass, null=True, blank=True, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=20, verbose_name="Sınıf Adı:", null=True)
    student_naame = models.CharField(max_length=20, verbose_name="Sınıf Adı:", null=True)
    student_name = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Öğrenci Adı")


class ClassHomework(models.Model):
    title = models.CharField(max_length=50, verbose_name="Başlık", null=True)
    content = RichTextField(null=True, blank=True, verbose_name="Ödev İçeriği")
    class_name = models.CharField(max_length=20, verbose_name="Sınıf Adı:", null=True)
    student_name = models.CharField(max_length=20, verbose_name="Öğrenci Adı:", null=True)
    classroom = models.ForeignKey(NewClass, null=True, blank=True, on_delete=models.CASCADE)
    student = models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True, null=True)
    end_date = models.DateField("Bitiş Tarihi(dd/mm/yyyy)", help_text="Lütfen formata uygun giriniz.",
                                auto_now_add=False, auto_now=False, null=True)
    end_clock = models.TimeField("Bitiş Saati(h:m:s)", help_text="Lütfen formata uygun giriniz.", auto_now_add=False,
                                 auto_now=False, null=True)
    files = models.FileField(upload_to='HomeWorks/', null=True, blank=True)
    is_deliver = models.BooleanField(null=True)
    is_end = models.BooleanField(null=True, default=0)
    note = models.IntegerField(blank=True, null=True)
    homework_code = models.CharField(max_length=6, null=True, blank=True)


class Homework(models.Model):
    title = models.CharField(max_length=50, verbose_name="Başlık", null=True)
    content = RichTextField(null=True, blank=True, verbose_name="Ödev İçeriği")
    classroom = models.ForeignKey(NewClass, null=True, blank=True, on_delete=models.CASCADE)
    end_date = models.DateField("Bitiş Tarihi(dd/mm/yyyy)", help_text="Lütfen formata uygun giriniz.",
                                auto_now_add=False, auto_now=False, null=True)
    end_clock = models.TimeField("Bitiş Saati(h:m:s)", help_text="Lütfen formata uygun giriniz.", auto_now_add=False,
                                 auto_now=False, null=True)
    is_end = models.BooleanField(null=True, default=0)
    homework_code = models.CharField(max_length=6, null=True, blank=True)
    submit_count = models.IntegerField(null=True, blank=True, verbose_name="Teslim Eden Sayısı")


class ClassPost(models.Model):
    title = models.CharField(max_length=50, verbose_name="Başlık", null=True)
    content = RichTextField(null=True, blank=True, verbose_name="Post")
    author = models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.CASCADE)
    classroom = models.ForeignKey(NewClass, null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    files = models.FileField(upload_to='Classes/Posts/', null=True, blank=True)
