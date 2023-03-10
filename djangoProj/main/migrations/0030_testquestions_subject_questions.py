# Generated by Django 4.1.7 on 2023-03-08 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_tests'),
    ]

    operations = [
        migrations.AddField(
            model_name='testquestions',
            name='subject',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.testsubject'),
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('opt_1', models.CharField(max_length=200)),
                ('opt_2', models.CharField(max_length=200)),
                ('opt_3', models.CharField(max_length=200)),
                ('opt_4', models.CharField(max_length=200)),
                ('right_opt', models.CharField(max_length=100)),
                ('test', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.tests')),
            ],
        ),
    ]
