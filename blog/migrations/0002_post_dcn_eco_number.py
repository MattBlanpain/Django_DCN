# Generated by Django 3.0.5 on 2020-04-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='DCN_ECO_number',
            field=models.CharField(default='', max_length=50),
        ),
    ]
