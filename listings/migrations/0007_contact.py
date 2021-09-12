# Generated by Django 3.0.4 on 2021-09-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20210912_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
