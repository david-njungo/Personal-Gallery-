# Generated by Django 3.0 on 2021-09-07 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_remove_image_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='article_image',
            new_name='image',
        ),
    ]
