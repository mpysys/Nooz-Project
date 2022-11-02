# Generated by Django 4.1.2 on 2022-10-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nooz2', '0010_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_media',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]