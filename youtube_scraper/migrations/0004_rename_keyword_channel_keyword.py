# Generated by Django 4.2.1 on 2023-05-07 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_scraper', '0003_rename_name_channel_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='KeyWord',
            new_name='keyword',
        ),
    ]
