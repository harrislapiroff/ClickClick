# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clickclick', '0002_auto_20140227_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='_order',
            field=models.OrderWrt(default=1),
            preserve_default=False,
        ),
    ]
