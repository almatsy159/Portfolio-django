# Generated by Django 5.0.4 on 2024-05-27 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0012_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='meta_doc_id',
        ),
    ]
