# Generated by Django 5.1.3 on 2024-11-13 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_articles_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articles',
            new_name='Article',
        ),
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
