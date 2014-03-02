# encoding: utf8
from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clickclick', '0004_auto_20140302_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=autoslug.fields.AutoSlugField(max_length=128),
        ),
    ]
