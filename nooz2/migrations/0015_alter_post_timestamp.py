# Generated by Django 4.1.2 on 2022-11-14 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nooz2', '0014_alter_post_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
