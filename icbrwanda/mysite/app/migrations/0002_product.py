# Generated by Django 4.1.3 on 2023-03-02 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('qty', models.TextField(null=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('crated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
