# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clickclick', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='photoset',
            unique_together=set([('owner', 'slug')]),
        ),
        migrations.AddField(
            model_name='photoset',
            name='privacy',
            field=models.CharField(default='PR', max_length=2, choices=[('PR', 'Private'), ('UN', 'Unlisted'), ('PL', 'Public')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photoset',
            name='slug',
            field=models.CharField(max_length=50),
        ),
    ]
