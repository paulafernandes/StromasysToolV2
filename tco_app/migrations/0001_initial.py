# Generated by Django 2.1.3 on 2018-11-30 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CpuTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_cpu', models.IntegerField(default=0)),
                ('max_cpu', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LicenceTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licence_name', models.CharField(max_length=50)),
                ('licence_cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ModelTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50)),
                ('power_name', models.CharField(max_length=50)),
                ('power_watt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SystemTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='modeltable',
            name='id_system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tco_app.SystemTable'),
        ),
        migrations.AddField(
            model_name='cputable',
            name='id_licence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tco_app.LicenceTable'),
        ),
        migrations.AddField(
            model_name='cputable',
            name='id_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tco_app.ModelTable'),
        ),
    ]
