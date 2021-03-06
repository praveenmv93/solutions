# Generated by Django 3.1.5 on 2021-01-26 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excellapp', '0004_auto_20210125_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=120, null=True)),
                ('project_client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='excellapp.client')),
            ],
        ),
        migrations.AddField(
            model_name='client_suggestion',
            name='projects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='excellapp.projects'),
        ),
        migrations.AddField(
            model_name='proj_sts',
            name='projects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='excellapp.projects'),
        ),
    ]
