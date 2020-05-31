# Generated by Django 3.0.3 on 2020-05-31 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200527_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(blank=True, help_text='Profil linkinizi koyunuz.', max_length=30, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='profile',
            name='github',
            field=models.CharField(blank=True, help_text='Profil linkinizi koyunuz.', max_length=30, null=True, verbose_name='Github'),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='İnstagram'),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(blank=True, help_text='Profil linkinizi koyunuz.', max_length=30, null=True, verbose_name='Linkedin'),
        ),
        migrations.AddField(
            model_name='profile',
            name='pinterest',
            field=models.CharField(blank=True, help_text='Profil linkinizi koyunuz.', max_length=30, null=True, verbose_name='Pinterest'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(blank=True, help_text='Profil linkinizi koyunuz.', max_length=30, null=True, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='high_school',
            field=models.CharField(blank=True, help_text='Profil linkinizi koyunuz.', max_length=50, null=True, verbose_name='Lise'),
        ),
    ]