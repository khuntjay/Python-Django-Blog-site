# Generated by Django 3.1.7 on 2021-03-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210322_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.CharField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
