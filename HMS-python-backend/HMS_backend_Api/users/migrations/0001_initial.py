# Generated by Django 3.2.21 on 2023-09-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=70)),
                ('lastname', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone_number', models.CharField(default='', max_length=20)),
                ('password', models.CharField(default='', max_length=70)),
            ],
        ),
    ]
