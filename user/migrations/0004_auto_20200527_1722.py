# Generated by Django 3.0.3 on 2020-05-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200527_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='end_date_high_school',
            field=models.DateField(blank=True, help_text='Lütfen formata uygun giriniz.', null=True, verbose_name='Bitiş Tarihi(mm/dd/yyyy)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='end_date_master_degree',
            field=models.DateField(blank=True, help_text='Lütfen formata uygun giriniz.', null=True, verbose_name='Bitiş Tarihi(mm/dd/yyyy)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='end_date_phd',
            field=models.DateField(blank=True, help_text='Lütfen formata uygun giriniz.', null=True, verbose_name='Bitiş Tarihi(mm/dd/yyyy)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='end_date_university',
            field=models.DateField(blank=True, help_text='Lütfen formata uygun giriniz.', null=True, verbose_name='Bitiş Tarihi(mm/dd/yyyy)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='started_date_high_school',
            field=models.DateField(blank=True, help_text='Lütfen formata uygun giriniz.', null=True, verbose_name='Başlangıç Tarihi(mm/dd/yyyy)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='started_date_master_degree',
            field=models.DateField(blank=True, help_text='Lütfen formata uygun giriniz.', null=True, verbose_name='Başlangıç Tarihi(mm/dd/yyyy)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='started_date_phd',
            field=models.DateField(blank=True, help_text='Lütfen formata uygun giriniz.', null=True, verbose_name='Başlangıç Tarihi(mm/dd/yyyy)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='started_date_university',
            field=models.DateField(blank=True, help_text='Lütfen formata uygun giriniz.', null=True, verbose_name='Başlangıç Tarihi(mm/dd/yyyy)'),
        ),
    ]