# Generated by Django 3.1.2 on 2020-10-12 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20201012_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joblist',
            name='register',
        ),
        migrations.RemoveField(
            model_name='startup',
            name='register',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
