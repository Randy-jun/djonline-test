# Generated by Django 2.1.1 on 2019-03-03 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='o_jieji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('line_num', models.CharField(max_length=128)),
                ('fee', models.FloatField()),
                ('address', models.CharField(max_length=256)),
                ('o_from', models.CharField(max_length=128)),
                ('o_to', models.CharField(max_length=128)),
                ('qifei_time', models.CharField(blank=True, max_length=128)),
                ('luodi_time', models.CharField(blank=True, max_length=128)),
                ('hangzhanlou', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='o_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(blank=True, max_length=128)),
                ('o_type', models.CharField(max_length=128)),
                ('o_from_org', models.CharField(max_length=128)),
                ('o_zhidan_time', models.DateTimeField()),
                ('o_zhidan', models.CharField(max_length=128)),
                ('o_tijiao', models.CharField(max_length=128, null=True)),
                ('o_tijiao_time', models.DateTimeField(null=True)),
                ('o_shouli', models.CharField(max_length=128, null=True)),
                ('o_fukuan', models.CharField(max_length=128, null=True)),
                ('o_shoukuan', models.CharField(max_length=128, null=True)),
                ('o_shoukuan_time', models.DateTimeField(null=True)),
                ('o_jiesuan_type', models.CharField(max_length=32, null=True)),
                ('o_dahui_msg', models.CharField(max_length=512, null=True)),
                ('o_status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='o_songji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('line_num', models.CharField(max_length=128)),
                ('fee', models.FloatField()),
                ('address', models.CharField(max_length=256)),
                ('o_from', models.CharField(blank=True, max_length=128)),
                ('o_to', models.CharField(blank=True, max_length=128)),
                ('qifei_time', models.CharField(max_length=128)),
                ('luodi_time', models.CharField(max_length=128)),
                ('hangzhanlou', models.CharField(max_length=32)),
                ('o_order', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.o_order')),
            ],
        ),
        migrations.CreateModel(
            name='o_tourist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=128)),
                ('number', models.IntegerField()),
                ('o_order', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.o_order')),
            ],
        ),
        migrations.AddField(
            model_name='o_jieji',
            name='o_order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.o_order'),
        ),
    ]
