# Generated by Django 4.0.4 on 2022-05-11 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_rename_name_bike_serialnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='bike',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rental.bike'),
        ),
    ]
