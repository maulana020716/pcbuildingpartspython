# Generated by Django 3.0.3 on 2020-07-03 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0005_auto_20200703_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='vga',
            name='color',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='vga',
            name='cool',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vga',
            name='display',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vga',
            name='display_port',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vga',
            name='dvi',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vga',
            name='ex_power',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='vga',
            name='expan_slot',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vga',
            name='frame_sync',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='vga',
            name='hdmi',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vga',
            name='hdmi_port',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vga',
            name='length',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=6),
        ),
        migrations.AddField(
            model_name='vga',
            name='mini_disp_port',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vga',
            name='mini_hdmi',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vga',
            name='sli',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='vga',
            name='tdp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vga',
            name='boost_clock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vga',
            name='core_clock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vga',
            name='vga_interface',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
