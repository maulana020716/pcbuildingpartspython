# Generated by Django 3.0.3 on 2020-07-03 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0003_auto_20200702_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='vga',
            name='eff_mem_clock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vga',
            name='manufacturer',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='vga',
            name='mem_type',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='vga',
            name='part',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='boost_clock',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=5),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='core_clock',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='socket',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
