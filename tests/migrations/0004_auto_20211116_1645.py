# Generated by Django 3.2.7 on 2021-11-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_auto_20211113_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='responses',
            name='correct_questions',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='responses',
            name='total_no_of_questions',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='test',
            name='accept',
            field=models.BooleanField(default=False),
        ),
    ]
