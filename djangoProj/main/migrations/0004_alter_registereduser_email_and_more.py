# Generated by Django 4.1.7 on 2023-02-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_passward_registereduser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registereduser',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='firstName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='lastName',
            field=models.CharField(max_length=50),
        ),
    ]