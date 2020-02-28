# Generated by Django 3.0.3 on 2020-02-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=250)),
                ('destination_name', models.CharField(max_length=250)),
                ('impact_type', models.CharField(max_length=250)),
                ('date', models.DateField()),
            ],
        ),
    ]