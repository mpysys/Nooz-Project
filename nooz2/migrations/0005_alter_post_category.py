# Generated by Django 4.1.2 on 2022-10-21 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nooz2', '0004_category_post_category_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='news', max_length=255),
        ),
    ]
