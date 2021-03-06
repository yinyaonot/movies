# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-11-24 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CateLog',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 't_cate_log',
            },
        ),
        migrations.CreateModel(
            name='Decade',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('is_use', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('sort', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_decade',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('actor', models.CharField(blank=True, max_length=255, null=True)),
                ('cata_log_name', models.CharField(max_length=255)),
                ('evaluation', models.FloatField()),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('is_use', models.IntegerField()),
                ('loc_name', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('plot', models.TextField(blank=True, null=True)),
                ('resolution', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_class_name', models.CharField(blank=True, max_length=255, null=True)),
                ('type_name', models.CharField(blank=True, max_length=255, null=True)),
                ('update_time', models.CharField(blank=True, max_length=255, null=True)),
                ('is_vip', models.IntegerField(blank=True, null=True)),
                ('cata_log', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.CateLog')),
            ],
            options={
                'db_table': 't_film',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('is_use', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 't_level',
            },
        ),
        migrations.CreateModel(
            name='Loc',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('is_use', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 't_loc',
            },
        ),
        migrations.CreateModel(
            name='Raty',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('en_time', models.CharField(blank=True, max_length=255, null=True)),
                ('score', models.CharField(blank=True, max_length=255, null=True)),
                ('film', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Film')),
            ],
            options={
                'db_table': 't_raty',
            },
        ),
        migrations.CreateModel(
            name='Res',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('episodes', models.IntegerField()),
                ('is_use', models.IntegerField()),
                ('link', models.TextField(blank=True, null=True)),
                ('link_type', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('update_time', models.CharField(blank=True, max_length=255, null=True)),
                ('film', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Film')),
            ],
            options={
                'db_table': 't_res',
            },
        ),
        migrations.CreateModel(
            name='SubClass',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('is_use', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('catalog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.CateLog')),
            ],
            options={
                'db_table': 't_subclass',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('is_use', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('subclass', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.SubClass')),
            ],
            options={
                'db_table': 't_type',
            },
        ),
        migrations.CreateModel(
            name='VipCode',
            fields=[
                ('id', models.CharField(max_length=225, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('is_use', models.CharField(blank=True, max_length=255, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('expire_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_vipcode',
            },
        ),
        migrations.AddField(
            model_name='film',
            name='loc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Loc'),
        ),
        migrations.AddField(
            model_name='film',
            name='on_decade',
            field=models.ForeignKey(blank=True, db_column='on_decade', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Decade'),
        ),
        migrations.AddField(
            model_name='film',
            name='sub_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.SubClass'),
        ),
        migrations.AddField(
            model_name='film',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Type'),
        ),
    ]
