# Generated by Django 3.2.7 on 2021-11-16 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_test_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='test',
        ),
        migrations.AddField(
            model_name='responses',
            name='test_submit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_submit', to='tests.test'),
        ),
    ]