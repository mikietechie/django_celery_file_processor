# Generated by Django 4.2.5 on 2023-10-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
