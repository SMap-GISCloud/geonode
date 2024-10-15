# Generated by Django 2.2.24 on 2022-02-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0046_auto_20210903_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('WMS', 'Web Map Service'), ('GN_WMS', 'SMap (Web Map Service)'), ('REST_MAP', 'ArcGIS REST MapServer'), ('REST_IMG', 'ArcGIS REST ImageServer')], max_length=10),
        ),
    ]
