# Generated by Django 3.0.3 on 2020-04-29 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classRoom', '0006_auto_20200429_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newclass',
            name='class_teacher_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yükleyen'),
        ),
    ]
