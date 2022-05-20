# Generated by Django 4.0 on 2022-05-20 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('active', models.BooleanField(default=True, verbose_name='Active?')),
                ('desc', models.CharField(max_length=525, verbose_name='Description')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IdiomsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Created')),
                ('modified', models.DateField(auto_now=True, verbose_name='Modified')),
                ('active', models.BooleanField(default=True, verbose_name='Active?')),
                ('lang', models.CharField(max_length=64, verbose_name='Language')),
                ('level', models.CharField(choices=[('Advanced', 'Advanced'), ('Intermediary', 'Intermediary'), ('Basic', 'Basic')], max_length=64, verbose_name='Level')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
