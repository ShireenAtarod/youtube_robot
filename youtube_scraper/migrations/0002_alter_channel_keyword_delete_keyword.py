# Generated by Django 4.2.1 on 2023-05-07 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_scraper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='KeyWord',
            field=models.TextField(max_length=100),
        ),
        migrations.DeleteModel(
            name='KeyWord',
        ),
    ]