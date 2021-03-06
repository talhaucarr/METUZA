# Generated by Django 3.0.3 on 2020-05-06 18:38

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classRoom', '0008_auto_20200429_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='classcontent',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classRoom.NewClass'),
        ),
        migrations.AddField(
            model_name='classhomework',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='classhomework',
            name='title',
            field=models.CharField(max_length=50, null=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='classhomework',
            name='end_date',
            field=models.DateField(null=True, verbose_name='mm/dd/yyyy'),
        ),
        migrations.AlterField(
            model_name='classhomework',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='HomeWorks/'),
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homework_name', models.CharField(max_length=50, verbose_name='Başlık')),
                ('classroom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classRoom.NewClass')),
            ],
        ),
    ]
