# Generated by Django 4.1.1 on 2022-09-21 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneview_page', '0016_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='company',
            field=models.CharField(default='company_or_institute', max_length=50, primary_key=True, serialize=False),
        ),
    ]
