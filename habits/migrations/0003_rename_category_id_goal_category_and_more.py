# Generated by Django 5.0.6 on 2024-05-16 03:58

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_auto_20240516_0250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='habit',
            old_name='category_id',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='categoryhabit',
            name='date_current',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='categoryhabit',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='goal',
            name='date_current',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='habit',
            name='date_current',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='month',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='StudyDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study_time', models.FloatField()),
                ('date_current', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits.categoryhabit')),
            ],
        ),
    ]