# Generated by Django 4.1.5 on 2023-01-25 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_pessoa_delete_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pessoa',
        ),
    ]