# Generated by Django 3.0.3 on 2020-07-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0002_auto_20200702_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpu',
            name='boost_clock',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=3),
        ),
        migrations.AddField(
            model_name='cpu',
            name='core_fam',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='cpu',
            name='ecc_sup',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='cpu',
            name='inc_cool',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='cpu',
            name='integ_graph',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='cpu',
            name='l1_cache',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='cpu',
            name='l2_cache',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='cpu',
            name='l3_cache',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='cpu',
            name='litho',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='cpu',
            name='manufacturer',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='cpu',
            name='max_sup_mem',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cpu',
            name='mic_arc',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='cpu',
            name='package',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='cpu',
            name='part',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='cpu',
            name='series',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='cpu',
            name='sim_multhread',
            field=models.CharField(default=None, max_length=150),
        ),
    ]