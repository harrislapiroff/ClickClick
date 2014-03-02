# encoding: utf8
from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clickclick', '0003_photo__order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='index',
        ),
        migrations.AlterField(
            model_name='photo',
            name='slug',
            field=autoslug.fields.AutoSlugField(max_length=128, editable=False),
        ),
        migrations.AlterField(
            model_name='photoset',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False),
        ),
    ]
