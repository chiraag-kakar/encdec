# Generated by Django 2.2.3 on 2019-07-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190702_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='alldata',
            name='finder',
            field=models.CharField(default='', max_length=50),
        ),
    ]
