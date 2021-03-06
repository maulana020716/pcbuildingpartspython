# Generated by Django 3.0.7 on 2020-07-01 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('socket', models.CharField(max_length=150)),
                ('mem_type', models.CharField(max_length=150)),
                ('vga_interface', models.CharField(max_length=150)),
                ('thumb_pic', models.ImageField(blank=True, upload_to='mtb/')),
                ('str_interface', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('chipset', models.CharField(max_length=150)),
                ('mem_cap', models.IntegerField()),
                ('core_clock', models.IntegerField()),
                ('boost_clock', models.IntegerField()),
                ('price', models.IntegerField()),
                ('thumb_pic', models.ImageField(blank=True, upload_to='vga/')),
                ('vga_interface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Motherboard')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mem_cap', models.IntegerField()),
                ('type', models.IntegerField()),
                ('cache', models.IntegerField()),
                ('price', models.IntegerField()),
                ('thumb_pic', models.ImageField(blank=True, upload_to='storage/')),
                ('str_interface', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Motherboard')),
            ],
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('mem_cap', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('module', models.IntegerField()),
                ('latency', models.IntegerField()),
                ('price', models.IntegerField()),
                ('thumb_pic', models.ImageField(blank=True, upload_to='ram/')),
                ('mem_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Motherboard')),
            ],
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('core_count', models.IntegerField()),
                ('core_clock', models.DecimalField(decimal_places=3, max_digits=3)),
                ('tdp', models.IntegerField()),
                ('price', models.IntegerField()),
                ('thumb_pic', models.ImageField(blank=True, upload_to='cpu/')),
                ('socket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sim.Motherboard')),
            ],
        ),
    ]
