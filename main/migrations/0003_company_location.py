# Generated by Django 3.0 on 2020-10-05 22:33

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_userprofile_user_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326),
        ),
    ]
