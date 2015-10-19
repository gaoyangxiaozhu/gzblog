# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_auto_20151017_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(blank=True, to='multblog.Article', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='relate_comment',
            field=models.ManyToManyField(to='comment.Comment', null=True, blank=True),
        ),
    ]
