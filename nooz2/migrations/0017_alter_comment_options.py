# Generated by Django 4.1.2 on 2022-11-15 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nooz2', '0016_alter_post_timestamp'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['timestamp']},
        ),
    ]