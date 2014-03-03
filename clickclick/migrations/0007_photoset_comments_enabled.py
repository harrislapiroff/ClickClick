# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clickclick', '0006_auto_20140302_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoset',
            name='comments_enabled',
            field=models.CharField(default='NO', max_length=2, verbose_name='Commenting', choices=[('ON', 'Enabled'), ('MD', 'Moderated'), ('NO', 'Disabled')]),
            preserve_default=True,
        ),
    ]
