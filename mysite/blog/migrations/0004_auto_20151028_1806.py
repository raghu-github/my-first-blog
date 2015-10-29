# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151028_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post1',
            name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='autho',
            new_name='author',
        ),
        migrations.DeleteModel(
            name='Post1',
        ),
    ]
