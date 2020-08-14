# Generated by Django 2.2 on 2020-08-13 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0009_simulation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulation',
            name='cpu_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='mtb_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='ram_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='str_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='simulation',
            name='vga_name',
            field=models.CharField(max_length=150),
        ),
    ]