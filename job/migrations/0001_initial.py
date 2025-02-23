# Generated by Django 5.1.6 on 2025-02-23 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('part-time', 'part-time'), ('full-time', 'full-time')], max_length=25)),
                ('description', models.CharField(max_length=1000)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('vacancy', models.IntegerField(default=1)),
                ('salary', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=1)),
            ],
        ),
    ]
