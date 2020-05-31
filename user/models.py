from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(upload_to='HomeWorks/', blank=True, null=True)


class Profile(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Ad", blank=True, null=True)
    surname = models.CharField(max_length=50, verbose_name="Soyad", blank=True, null=True)
    email = models.EmailField(max_length=50, verbose_name="E-mail", blank=True, null=True)
    about = models.CharField(max_length=150, verbose_name="Hakkında", blank=True, null=True)
    photo = models.FileField(upload_to='Photo/', blank=True, null=True)
    instagram = models.CharField(max_length=30, verbose_name="İnstagram", blank=True, null=True)
    github = models.CharField(max_length=30, verbose_name="Github", blank=True, null=True,
                              help_text="Profil linkinizi koyunuz.")
    twitter = models.CharField(max_length=30, verbose_name="Twitter", blank=True, null=True,
                               help_text="Profil linkinizi koyunuz.")
    facebook = models.CharField(max_length=30, verbose_name="Facebook", blank=True, null=True,
                                help_text="Profil linkinizi koyunuz.")
    linkedin = models.CharField(max_length=30, verbose_name="Linkedin", blank=True, null=True,
                                help_text="Profil linkinizi koyunuz.")
    pinterest = models.CharField(max_length=30, verbose_name="Pinterest", blank=True, null=True,
                                 help_text="Profil linkinizi koyunuz.")
    high_school = models.CharField(max_length=50, verbose_name="Lise", blank=True, null=True,
                                   help_text="Profil linkinizi koyunuz.")
    started_date_high_school = models.DateField("Başlangıç Tarihi(mm/dd/yyyy)",
                                                help_text="Lütfen formata uygun giriniz.",
                                                auto_now_add=False, auto_now=False, null=True, blank=True)

    end_date_high_school = models.DateField("Bitiş Tarihi(mm/dd/yyyy)", help_text="Lütfen formata uygun giriniz.",
                                            auto_now_add=False, auto_now=False, null=True, blank=True)

    university = models.CharField(max_length=50, verbose_name="Üniversite", blank=True, null=True)
    started_date_university = models.DateField("Başlangıç Tarihi(mm/dd/yyyy)",
                                               help_text="Lütfen formata uygun giriniz.",
                                               auto_now_add=False, auto_now=False, null=True, blank=True)

    end_date_university = models.DateField("Bitiş Tarihi(mm/dd/yyyy)", help_text="Lütfen formata uygun giriniz.",
                                           auto_now_add=False, auto_now=False, null=True, blank=True)

    master_degree = models.CharField(max_length=50, verbose_name="Yüksek Lisans", blank=True, null=True)
    started_date_master_degree = models.DateField("Başlangıç Tarihi(mm/dd/yyyy)",
                                                  help_text="Lütfen formata uygun giriniz.",
                                                  auto_now_add=False, auto_now=False, null=True, blank=True)

    end_date_master_degree = models.DateField("Bitiş Tarihi(mm/dd/yyyy)", help_text="Lütfen formata uygun giriniz.",
                                              auto_now_add=False, auto_now=False, null=True, blank=True)

    phd = models.CharField(max_length=50, verbose_name="Doktora", blank=True, null=True)
    started_date_phd = models.DateField("Başlangıç Tarihi(mm/dd/yyyy)", help_text="Lütfen formata uygun giriniz.",
                                        auto_now_add=False, auto_now=False, null=True, blank=True)

    end_date_phd = models.DateField("Bitiş Tarihi(mm/dd/yyyy)", help_text="Lütfen formata uygun giriniz.",
                                    auto_now_add=False, auto_now=False, null=True, blank=True)


class WorkExperience(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    company = models.CharField(max_length=50, verbose_name="Şirket Adı")
    position = models.CharField(max_length=50, verbose_name="Pozisyon")
    started_date = models.DateField("Başlangıç Tarihi(mm/dd/yyyy)", help_text="Lütfen formata uygun giriniz.",
                                    auto_now_add=False, auto_now=False, null=True)

    end_date = models.DateField("Bitiş Tarihi(mm/dd/yyyy)", help_text="Lütfen formata uygun giriniz.",
                                auto_now_add=False, auto_now=False, null=True)

# Create your models here.
