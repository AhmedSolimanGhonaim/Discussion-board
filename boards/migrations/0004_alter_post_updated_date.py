# Generated by Django 5.2 on 2025-04-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_post_updated_by_post_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
