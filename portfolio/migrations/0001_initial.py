# Generated by Django 4.1.5 on 2023-02-01 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('meta_type', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/work')),
                ('website_url', models.URLField(blank=True)),
                ('gitpod_url', models.URLField(blank=True)),
            ],
        ),
    ]