# Generated by Django 4.1.1 on 2022-09-21 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneview_page', '0013_alter_memory_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('title', models.CharField(default='career_title', max_length=100, primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField()),
                ('industrial', models.CharField(max_length=30)),
                ('role_of_participants', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=200)),
                ('aim_of_earning', models.FloatField()),
            ],
        ),
    ]
