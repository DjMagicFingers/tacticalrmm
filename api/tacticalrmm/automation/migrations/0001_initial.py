# Generated by Django 3.0.4 on 2020-04-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('desc', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('agents', models.ManyToManyField(related_name='policies', to='agents.Agent')),
                ('clients', models.ManyToManyField(related_name='policies', to='clients.Client')),
                ('sites', models.ManyToManyField(related_name='policies', to='clients.Site')),
            ],
        ),
    ]
