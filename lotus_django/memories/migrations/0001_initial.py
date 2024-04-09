# Generated by Django 2.2 on 2024-04-05 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memoryID', models.CharField(max_length=100)),
                ('entryID', models.CharField(max_length=100)),
                ('emotion', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]