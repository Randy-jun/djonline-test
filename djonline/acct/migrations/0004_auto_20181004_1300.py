# Generated by Django 2.1.1 on 2018-10-04 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acct', '0003_auto_20181004_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency_t',
            name='localname',
            field=models.CharField(default='中国国际旅行社', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application_t',
            name='localname',
            field=models.CharField(default='中国国际旅行社', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='line_price_t',
            name='localname',
            field=models.CharField(default='中国国际旅行社', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ref_price_t',
            name='localname',
            field=models.CharField(default='中国国际旅行社', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settlement_t',
            name='localname',
            field=models.CharField(default='中国国际旅行社', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tourist_t',
            name='localname',
            field=models.CharField(default='中国国际旅行社', max_length=128),
            preserve_default=False,
        ),
    ]