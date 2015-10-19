# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='comment_people',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='reComment',
            new_name='relate_omment',
        ),
    ]
