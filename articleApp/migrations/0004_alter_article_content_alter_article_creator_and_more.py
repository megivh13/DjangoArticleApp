# Generated by Django 5.1.5 on 2025-01-25 15:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleApp', '0003_article_creator_alter_article_word_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, default='', verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='creator'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='twitter_post',
            field=models.TextField(blank=True, default='', verbose_name='twitter_post'),
        ),
        migrations.AlterField(
            model_name='article',
            name='word_count',
            field=models.IntegerField(blank=True, default='', verbose_name='word_count'),
        ),
    ]
