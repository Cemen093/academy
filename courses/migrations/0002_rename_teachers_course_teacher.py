# Generated by Django 3.2.2 on 2021-05-13 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='teachers',
            new_name='teacher',
        ),
    ]
