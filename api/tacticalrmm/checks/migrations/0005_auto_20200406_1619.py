# Generated by Django 3.0.4 on 2020-04-06 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0001_initial'),
        ('checks', '0004_auto_20200406_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpuloadcheck',
            name='policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='automation.Policy'),
        ),
        migrations.AddField(
            model_name='diskcheck',
            name='policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='automation.Policy'),
        ),
        migrations.AddField(
            model_name='memcheck',
            name='policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='automation.Policy'),
        ),
        migrations.AddField(
            model_name='pingcheck',
            name='policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='automation.Policy'),
        ),
        migrations.AddField(
            model_name='scriptcheck',
            name='policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='automation.Policy'),
        ),
        migrations.AddField(
            model_name='winservicecheck',
            name='policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='automation.Policy'),
        ),
    ]
