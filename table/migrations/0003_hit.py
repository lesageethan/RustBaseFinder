# Generated by Django 3.0.5 on 2020-05-17 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_base_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=16)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
