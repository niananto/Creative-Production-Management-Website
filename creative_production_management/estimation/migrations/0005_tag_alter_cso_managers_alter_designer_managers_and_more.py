# Generated by Django 4.1.7 on 2023-02-28 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estimation', '0004_cso_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterModelManagers(
            name='cso',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='designer',
            managers=[
            ],
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.CreateModel(
            name='Estimation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('estimated_duration_months', models.IntegerField()),
                ('estimated_cost', models.FloatField()),
                ('cso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estimation.cso')),
                ('designers', models.ManyToManyField(to='estimation.designer')),
                ('tags', models.ManyToManyField(to='estimation.tag')),
                ('vendors', models.ManyToManyField(to='estimation.vendor')),
            ],
        ),
        migrations.AddField(
            model_name='designer',
            name='tag',
            field=models.ManyToManyField(to='estimation.tag'),
        ),
    ]
