from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Forum(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(upload_to='Posts/', null=True, blank=True, verbose_name="")

    def __str__(self):
        return self.title


class Comment(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name="comments")
    comment_author = models.CharField("auth.User", max_length=50)
    comment_content = models.CharField(max_length=200,)
    comment_date = models.DateTimeField(auto_now_add=True)
