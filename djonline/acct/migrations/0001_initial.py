# Generated by Django 2.1.1 on 2019-02-11 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency_t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('remark', models.CharField(blank=True, default='', max_length=256)),
                ('local_agency_fk', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '组织信息 (Agency_t)',
                'verbose_name_plural': '组织信息表 (Agency_t)',
            },
        ),
        migrations.CreateModel(
            name='Application_t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('status', models.CharField(default='0', max_length=32)),
                ('agency_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acct.Agency_t')),
            ],
            options={
                'verbose_name': '出团申请单 (Application_t)',
                'verbose_name_plural': '出团申请单表 (Application_t)',
            },
        ),
        migrations.CreateModel(
            name='DjUser_t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('token', models.CharField(default='', max_length=1024)),
                ('is_logged', models.BooleanField(default=False)),
                ('nick_name', models.CharField(default='nick name', max_length=128)),
                ('e_mail', models.EmailField(default='dj@dj.com.cn', max_length=254)),
                ('local_agency_fk', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='acct.Agency_t')),
            ],
            options={
                'verbose_name': '用户信息 (DjUser_t)',
                'verbose_name_plural': '用户信息表 (DjUser_t)',
            },
        ),
        migrations.CreateModel(
            name='Line_Price_t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('remark', models.CharField(blank=True, max_length=128)),
                ('detail', models.TextField(blank=True, max_length=2048)),
                ('local_agency_fk', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='acct.Agency_t')),
            ],
            options={
                'verbose_name': '线路报价 (Line_Price_t)',
                'verbose_name_plural': '线路报价表 (Line_Price_t)',
            },
        ),
        migrations.CreateModel(
            name='Ref_Price_t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=64)),
                ('price', models.FloatField()),
                ('line_price_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acct.Line_Price_t')),
                ('local_agency_fk', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='acct.Agency_t')),
            ],
            options={
                'verbose_name': '参考报价 (Ref_Price_t)',
                'verbose_name_plural': '参考报价表 (Ref_Price_t)',
            },
        ),
        migrations.CreateModel(
            name='Settlement_t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('kind', models.CharField(max_length=64)),
                ('application_t', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='acct.Application_t')),
                ('local_agency_fk', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='acct.Agency_t')),
                ('pay_agency_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pay_agency', to='acct.Agency_t')),
                ('rec_agency_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='rec_agency', to='acct.Agency_t')),
            ],
            options={
                'verbose_name': '结算信息 (Settlement_t)',
                'verbose_name_plural': '结算信息表 (Settlement_t)',
            },
        ),
        migrations.CreateModel(
            name='Tourist_t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('amount', models.IntegerField(default=1)),
                ('fix_price', models.FloatField(default=0)),
                ('final_price', models.FloatField(default=0)),
                ('fix_remark', models.CharField(blank=True, max_length=128)),
                ('trans_price', models.FloatField(default=0)),
                ('trans_remark', models.CharField(blank=True, max_length=128)),
                ('trans_agency', models.CharField(default='0', max_length=128)),
                ('agent_price', models.FloatField(default=0)),
                ('agent_remark', models.CharField(blank=True, max_length=128)),
                ('application_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acct.Application_t')),
                ('local_agency_fk', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='acct.Agency_t')),
                ('ref_price_fk', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acct.Ref_Price_t')),
            ],
            options={
                'verbose_name': '游客信息 (Tourist_t)',
                'verbose_name_plural': '游客信息表 (Tourist_t)',
            },
        ),
        migrations.AddField(
            model_name='application_t',
            name='def_price_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acct.Ref_Price_t'),
        ),
        migrations.AddField(
            model_name='application_t',
            name='line_name_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='acct.Line_Price_t'),
        ),
        migrations.AddField(
            model_name='application_t',
            name='local_agency_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='local', to='acct.Agency_t'),
        ),
        migrations.AlterUniqueTogether(
            name='agency_t',
            unique_together={('name', 'local_agency_fk')},
        ),
        migrations.AlterUniqueTogether(
            name='ref_price_t',
            unique_together={('kind', 'local_agency_fk', 'line_price_fk')},
        ),
        migrations.AlterUniqueTogether(
            name='line_price_t',
            unique_together={('name', 'local_agency_fk')},
        ),
        migrations.AlterUniqueTogether(
            name='djuser_t',
            unique_together={('name', 'local_agency_fk')},
        ),
    ]
