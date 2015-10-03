# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0007_auto_20150923_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalresult',
            name='endtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 26, 1, 58, 22, 939132, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='finalresult',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 26, 1, 58, 22, 939107, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='groupfinalresult',
            name='endtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 26, 1, 58, 22, 937925, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='groupfinalresult',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 26, 1, 58, 22, 937891, tzinfo=utc)),
        ),
    ]
