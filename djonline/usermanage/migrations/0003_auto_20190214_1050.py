# Generated by Django 2.1.5 on 2019-02-14 02:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usermanage', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('remark', models.CharField(blank=True, default='', max_length=256)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': '组织信息表 (organization)',
            },
        ),
        migrations.CreateModel(
            name='partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_level', models.IntegerField(default=1)),
                ('p_remark', models.CharField(blank=True, default='', max_length=256)),
                ('p_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermanage.organization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='伙伴')),
            ],
            options={
                'verbose_name_plural': '伙伴',
            },
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name_plural': '职员'},
        ),
        migrations.AddField(
            model_name='employee',
            name='e_remark',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermanage.organization'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='e_type',
            field=models.IntegerField(default=1),
        ),
    ]
