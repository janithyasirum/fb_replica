# Generated by Django 2.0 on 2017-12-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_auto_20171211_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='postfiles',
            name='file_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
