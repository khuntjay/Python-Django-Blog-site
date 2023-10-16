# Generated by Django 3.1.7 on 2021-03-22 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact_issu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=254)),
                ('content', models.TextField()),
                ('autho', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='issu',
            field=models.CharField(default='', max_length=300),
        ),
    ]