# Generated by Django 3.2.7 on 2021-11-16 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0007_auto_20211116_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responses',
            name='test_submit',
        ),
    ]
