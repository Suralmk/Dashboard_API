# Generated by Django 5.0.6 on 2024-05-30 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_statstics_added_alter_statstics_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statstics',
            name='end_year',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='statstics',
            name='start_year',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]