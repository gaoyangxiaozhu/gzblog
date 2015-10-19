# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0005_auto_20151017_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='relate_comment',
            field=models.ManyToManyField(to='comment.Comment', blank=True),
        ),
    ]
