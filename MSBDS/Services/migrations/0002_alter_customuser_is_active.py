# Generated by Django 4.2.5 on 2023-09-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
