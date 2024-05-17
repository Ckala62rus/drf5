# Generated by Django 5.0.6 on 2024-05-13 18:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(help_text='Title for your post', max_length=150, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='name',
            field=models.CharField(help_text='Title', max_length=150, unique=True, verbose_name='Название Статьи'),
        ),
    ]