# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0005_auto_20150917_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='mean',
            field=models.TextField(default=0, max_length=300),
        ),
        migrations.AlterField(
            model_name='finalresult',
            name='endtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 9, 3, 47, 745282, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='finalresult',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 9, 3, 47, 745256, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='groupfinalresult',
            name='endtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 9, 3, 47, 744052, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='groupfinalresult',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 9, 3, 47, 744017, tzinfo=utc)),
        ),
    ]
