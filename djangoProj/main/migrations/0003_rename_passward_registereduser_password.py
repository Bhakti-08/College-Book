# Generated by Django 4.1.7 on 2023-02-25 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_registereduser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registereduser',
            old_name='passward',
            new_name='password',
        ),
    ]
