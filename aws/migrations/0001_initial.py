# Generated by Django 4.2.2 on 2023-06-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AWSKEY',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=50)),
                ('aws_access', models.CharField(max_length=40)),
                ('aws_secret', models.CharField(max_length=50)),
                ('aws_token', models.CharField(max_length=900)),
                ('aws_region', models.CharField(max_length=20)),
                ('aws_profile', models.CharField(max_length=40)),
            ],
        ),
    ]