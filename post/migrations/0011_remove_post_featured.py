# Generated by Django 2.2 on 2019-09-28 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_remove_post_comment_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured',
        ),
    ]