# Generated by Django 4.2.17 on 2025-01-09 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_challenge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='challenge',
        ),
    ]
