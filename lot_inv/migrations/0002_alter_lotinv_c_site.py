# Generated by Django 3.2.8 on 2021-10-27 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lot_inv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lotinv',
            name='c_site',
            field=models.IntegerField(choices=[('152', 'CBP')], null=True, verbose_name='site'),
        ),
    ]
