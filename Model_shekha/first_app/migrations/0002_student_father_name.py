# Generated by Django 5.0 on 2023-12-27 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.TextField(default='rahim'),
            preserve_default=False,
        ),
    ]
