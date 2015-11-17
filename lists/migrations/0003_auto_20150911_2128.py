# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_auto_20150911_2125'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listing',
            new_name='List',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='listing',
            new_name='list',
        ),
    ]
