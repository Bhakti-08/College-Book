# Generated by Django 4.1.7 on 2023-03-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_questions_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='opt_1',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='opt_2',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='opt_3',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='opt_4',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='questions',
            name='right_opt',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
