# Generated by Django 4.0 on 2024-03-18 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0005_alter_comment_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(default=''),
        ),
    ]