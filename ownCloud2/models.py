from django.db import models
from django.contrib.auth.models import User


class Cloud(models.Model):
    authorr = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yükleyen")
    title = models.CharField(max_length=100, blank=True, null=True)
    pdf = models.FileField(upload_to='DenemeKlasor/Dosyalar', )


    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

# Create your models here.