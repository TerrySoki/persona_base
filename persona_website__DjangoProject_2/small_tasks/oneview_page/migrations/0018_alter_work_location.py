# Generated by Django 4.1.1 on 2022-09-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneview_page', '0017_alter_work_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
