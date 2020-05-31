# Generated by Django 3.0.3 on 2020-05-30 20:43

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_content', ckeditor.fields.RichTextField()),
                ('files', models.FileField(blank=True, null=True, upload_to='Messages/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Gönderim Tarihi')),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Alıcı', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Gönderen', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
