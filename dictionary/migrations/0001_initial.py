# Generated by Django 3.1.2 on 2020-10-06 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qom', models.CharField(blank=True, max_length=100, null=True)),
                ('dfs', models.TextField(blank=True, null=True)),
                ('syn', models.CharField(blank=True, max_length=300, null=True)),
                ('var', models.CharField(blank=True, max_length=300, null=True)),
                ('see', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
