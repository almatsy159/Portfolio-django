# Generated by Django 5.0.4 on 2024-04-30 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0002_type_alter_document_content_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='doc_id',
            field=models.ManyToManyField(to='doc.document'),
        ),
    ]
