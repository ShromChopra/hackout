# Generated by Django 3.1.3 on 2020-11-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_location_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='area',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
