from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Msg(models.Model):
    sender = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="Gönderen")
    reciever = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="Alıcı")
    username = models.CharField(max_length=50, verbose_name="Kullanıcı Adı")
    msg_content = RichTextField()
    files = models.FileField(upload_to='Messages/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Gönderim Tarihi")
