# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(default=b'write some content in here!')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'live', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('intro', models.CharField(max_length=200)),
                ('current_job', models.CharField(max_length=100)),
                ('avatar', models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='multblog.UserAccount'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='multblog.Categories'),
        ),
    ]
