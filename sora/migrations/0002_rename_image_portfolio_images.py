# Generated by Django 4.1.5 on 2023-05-11 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sora', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='image',
            new_name='images',
        ),
    ]
