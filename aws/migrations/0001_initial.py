# Generated by Django 4.2.2 on 2023-08-27 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AWSKEY',
            fields=[
                ('idx', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('aws_access', models.CharField(default='', max_length=40)),
                ('aws_secret', models.CharField(default='', max_length=50)),
                ('aws_token', models.CharField(default='', max_length=900)),
                ('aws_region', models.CharField(default='', max_length=20)),
                ('aws_profile', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='EC2',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('MyResourceName', models.CharField(default='', max_length=20)),
                ('MyResourceType', models.CharField(default='', max_length=10)),
                ('MyResourceDetails', models.CharField(default='', max_length=10)),
                ('MyResourceGrade', models.CharField(default='', max_length=10)),
                ('PlatformDetails', models.CharField(default='', max_length=20)),
                ('InstanceId', models.CharField(default='', max_length=30)),
                ('KeyName', models.CharField(default='', max_length=20)),
                ('InstanceType', models.CharField(default='', max_length=15)),
                ('AvailabilityZone', models.CharField(default='', max_length=20)),
                ('PrivateIp', models.CharField(default='', max_length=20)),
                ('PbulicIp', models.CharField(default='', max_length=20)),
                ('PublicDns', models.CharField(default='', max_length=100)),
                ('Tags', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='IAMDB',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
                ('UserName', models.CharField(default='', max_length=30)),
                ('UserId', models.CharField(default='', max_length=21)),
                ('CreateDate', models.DateField()),
                ('PasswordLastUsed', models.DateTimeField()),
                ('ARN', models.CharField(default='', max_length=2048)),
                ('MinimumPasswordLength', models.IntegerField()),
                ('RequireLowercaseCharacters', models.IntegerField()),
                ('RequireUppercaseCharacters', models.IntegerField()),
                ('RequireNumbers', models.IntegerField()),
                ('RequireSymbols', models.IntegerField()),
                ('ExpirePasswords', models.IntegerField()),
                ('MaxPasswordAge', models.IntegerField()),
                ('PasswordReusePrevention', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IAMGROUPS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='IAMMFA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NETDB',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='S3DB',
            fields=[
                ('idx', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
