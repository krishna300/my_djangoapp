# Generated by Django 2.1.5 on 2019-09-08 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(null=True, upload_to='property/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('m', 'medium'), ('b', 'big'), ('s', 'small')], max_length=20),
        ),
    ]
