# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('email', models.CharField(max_length=100)),
                ('webSite', models.CharField(max_length=100)),
                ('article', models.ForeignKey(to='multblog.Article')),
                ('reComment', models.ManyToManyField(to='comment.Comment')),
            ],
        ),
    ]
