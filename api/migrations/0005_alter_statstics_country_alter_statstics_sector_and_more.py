# Generated by Django 5.0.6 on 2024-05-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_statstics_added_alter_statstics_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statstics',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='statstics',
            name='sector',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='statstics',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
