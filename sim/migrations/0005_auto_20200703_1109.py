# Generated by Django 3.0.3 on 2020-07-03 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0004_auto_20200703_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='boost_clock',
            field=models.DecimalField(decimal_places=1, default=None, max_digits=3),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='core_clock',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
