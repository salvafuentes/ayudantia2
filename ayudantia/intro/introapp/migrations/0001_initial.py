# Generated by Django 3.1.4 on 2022-09-29 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
