# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-25 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=244)),
                ('description', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='photos/')),
                ('categories', models.ManyToManyField(to='gallery.Category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Location')),
            ],
        ),
    ]
