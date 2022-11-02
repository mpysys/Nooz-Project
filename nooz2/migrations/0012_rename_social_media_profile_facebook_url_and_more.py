# Generated by Django 4.1.2 on 2022-10-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nooz2', '0011_profile_profile_pic_profile_social_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_media',
            new_name='facebook_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='site_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]