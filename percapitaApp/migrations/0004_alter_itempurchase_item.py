# Generated by Django 4.0.6 on 2022-10-01 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('percapitaApp', '0003_alter_itempurchase_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempurchase',
            name='item',
            field=models.CharField(max_length=50),
        ),
    ]
