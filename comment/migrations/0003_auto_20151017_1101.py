# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20151017_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='relate_omment',
            new_name='relate_comment',
        ),
    ]
