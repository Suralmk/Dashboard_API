# Generated by Django 5.0.6 on 2024-05-29 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statstics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=100)),
                ('pestle', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=50)),
                ('insight', models.CharField(max_length=200)),
                ('impact', models.CharField(max_length=200)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('published', models.DateTimeField()),
                ('added', models.DateTimeField()),
                ('relevance', models.IntegerField()),
                ('intensity', models.IntegerField()),
                ('likelihood', models.IntegerField()),
                ('url', models.URLField()),
            ],
        ),
    ]