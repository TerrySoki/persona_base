# Generated by Django 4.1.1 on 2022-09-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneview_page', '0018_alter_work_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
