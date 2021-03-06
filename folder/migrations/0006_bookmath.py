# Generated by Django 3.0.3 on 2020-03-22 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder', '0005_auto_20200322_0438'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookMath',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='books/pdfs/ScienceBook/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='books/covers/ScienceBook/')),
            ],
        ),
    ]
