# Generated by Django 4.0 on 2024-03-22 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0006_alter_comment_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_time']},
        ),
    ]
