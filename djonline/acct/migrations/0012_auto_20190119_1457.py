# Generated by Django 2.1.1 on 2019-01-19 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acct', '0011_auto_20181021_0939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency_t',
            options={'verbose_name': '组织信息 (Agency_t)', 'verbose_name_plural': '组织信息表 (Agency_t)'},
        ),
        migrations.AlterModelOptions(
            name='application_t',
            options={'verbose_name': '出团申请单 (Application_t)', 'verbose_name_plural': '出团申请单表 (Application_t)'},
        ),
        migrations.AlterModelOptions(
            name='djuser_t',
            options={'verbose_name': '用户信息 (DjUser_t)', 'verbose_name_plural': '用户信息表 (DjUser_t)'},
        ),
        migrations.AlterModelOptions(
            name='line_price_t',
            options={'verbose_name': '线路报价 (Line_Price_t)', 'verbose_name_plural': '线路报价表 (Line_Price_t)'},
        ),
        migrations.AlterModelOptions(
            name='ref_price_t',
            options={'verbose_name': '参考报价 (Ref_Price_t)', 'verbose_name_plural': '参考报价表 (Ref_Price_t)'},
        ),
        migrations.AlterModelOptions(
            name='settlement_t',
            options={'verbose_name': '结算信息 (Settlement_t)', 'verbose_name_plural': '结算信息表 (Settlement_t)'},
        ),
        migrations.AlterModelOptions(
            name='tourist_t',
            options={'verbose_name': '游客信息 (Tourist_t)', 'verbose_name_plural': '游客信息表 (Tourist_t)'},
        ),
    ]