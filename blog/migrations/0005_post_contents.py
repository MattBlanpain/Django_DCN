# Generated by Django 3.0.5 on 2020-04-22 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200422_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='contents',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
