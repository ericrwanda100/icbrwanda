# Generated by Django 4.1.3 on 2023-06-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='shema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('update', models.DateTimeField(auto_now=True)),
                ('crated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]