# Generated by Django 3.0 on 2020-02-04 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_articlecomment_category_message_tag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
