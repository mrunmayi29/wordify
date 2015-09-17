# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_auto_20150911_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalresult',
            name='endtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 9, 0, 28, 720437, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='finalresult',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 9, 0, 28, 720411, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='groupfinalresult',
            name='endtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 9, 0, 28, 719244, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='groupfinalresult',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 9, 0, 28, 719213, tzinfo=utc)),
        ),
    ]
