# Generated by Django 2.1.5 on 2019-02-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0006_auto_20190217_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='delete_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='delete_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='u_token_list',
            name='gen_date',
            field=models.DateTimeField(),
        ),
    ]
