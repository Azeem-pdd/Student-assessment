# Generated by Django 3.2.7 on 2021-11-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0010_testdetails_selections'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responses',
            name='test1',
        ),
        migrations.RemoveField(
            model_name='testdetails',
            name='selections',
        ),
        migrations.AddField(
            model_name='responses',
            name='selections',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]