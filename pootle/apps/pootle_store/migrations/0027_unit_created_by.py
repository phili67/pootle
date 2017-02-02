# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 21:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import pootle.core.user


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pootle_store', '0026_suggestion_on_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='created_by',
            field=models.ForeignKey(default=pootle.core.user.get_system_user_id, null=True, on_delete=models.SET(pootle.core.user.get_system_user), related_name='units_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
