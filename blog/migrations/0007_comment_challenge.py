# Generated by Django 4.2.17 on 2025-01-09 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='challenge',
            field=models.SlugField(default='test-slug'),
            preserve_default=False,
        ),
    ]
