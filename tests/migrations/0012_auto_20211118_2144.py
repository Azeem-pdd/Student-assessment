# Generated by Django 3.2.7 on 2021-11-18 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0011_auto_20211118_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responses',
            name='selections',
        ),
        migrations.CreateModel(
            name='Selcted_choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.PositiveIntegerField(blank=True, null=True)),
                ('res_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.responses')),
            ],
        ),
    ]
