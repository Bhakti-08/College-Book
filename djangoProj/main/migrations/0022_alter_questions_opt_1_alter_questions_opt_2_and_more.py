# Generated by Django 4.1.7 on 2023-03-06 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_questions_opt_1_alter_questions_opt_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='opt_1',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='opt_2',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='opt_3',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='opt_4',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='right_opt',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]