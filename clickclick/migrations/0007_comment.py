# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clickclick', '0006_auto_20140302_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id', null=True)),
                ('photo', models.ForeignKey(to='clickclick.Photo', to_field=u'id')),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
                ('email', models.EmailField(max_length=255, null=True, blank=True)),
                ('content', models.TextField()),
                ('submit_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('is_public', models.BooleanField(default=True)),
                ('is_removed', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
