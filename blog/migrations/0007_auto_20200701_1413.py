# Generated by Django 3.0.7 on 2020-07-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200625_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb_pic',
            field=models.ImageField(blank=True, upload_to='thumb_pic/'),
        ),
    ]
