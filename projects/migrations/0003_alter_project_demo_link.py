# Generated by Django 3.2.8 on 2021-11-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20211101_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
