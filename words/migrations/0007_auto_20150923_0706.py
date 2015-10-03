# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0006_auto_20150917_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalresult',
            name='endtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 23, 1, 36, 34, 618579, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='finalresult',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 23, 1, 36, 34, 618553, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='groupfinalresult',
            name='endtime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 23, 1, 36, 34, 617398, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='groupfinalresult',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 23, 1, 36, 34, 617369, tzinfo=utc)),
        ),
    ]
