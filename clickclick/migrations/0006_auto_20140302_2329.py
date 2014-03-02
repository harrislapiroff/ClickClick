# encoding: utf8
from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clickclick', '0005_auto_20140302_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoset',
            name='slug',
            field=autoslug.fields.AutoSlugField(),
        ),
    ]
