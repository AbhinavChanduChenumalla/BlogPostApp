# Generated by Django 2.2 on 2020-08-06 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200806_1852'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
    ]