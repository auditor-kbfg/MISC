from django.db import models
from users.models import USERS
import json

from web import settings
# Create your models here.
class AWSKEY(models.Model):
    # idx = models.BigAutoField( primary_key=True)
    idx = models.IntegerField( primary_key=True,default=1)
    aws_access=models.CharField(max_length=40,default='')
    aws_secret=models.CharField(max_length=50,default='')
    aws_token=models.CharField(max_length=900,default='')
    aws_region=models.CharField(max_length=20,default='')
    aws_profile=models.CharField(max_length=40,default='')
class EC2(models.Model):
    idx=models.BigAutoField(primary_key=True)
    MyResourceName=models.CharField(max_length=20,default='')
    MyResourceType=models.CharField(max_length=10,default='')
    MyResourceDetails=models.CharField(max_length=10,default='')
    MyResourceGrade=models.CharField(max_length=10,default='')
    PlatformDetails=models.CharField(max_length=20,default='')
    InstanceId=models.CharField(max_length=30,default='')
    KeyName=models.CharField(max_length=20,default='')
    InstanceType=models.CharField(max_length=15,default='')
    AvailabilityZone=models.CharField(max_length=20,default='')
    PrivateIp=models.CharField(max_length=20,default='')
    PbulicIp=models.CharField(max_length=20,default='')
    PublicDns=models.CharField(max_length=100,default='')
    Tags=models.TextField(default='')
    def get_Tags(self):
        return json.loads(self.Tags)
    def set_Tags(self,tags:list):
        self.Tags=json.dumps(tags)
class S3DB(models.Model):
    idx=models.BigAutoField(primary_key=True)
    
class NETDB(models.Model):
    idx=models.BigAutoField(primary_key=True)
    
class IAMDB(models.Model):
    idx=models.BigAutoField(primary_key=True)
    UserName = models.CharField(max_length=30,default='')
    UserId = models.CharField(max_length=21,default='')
    CreateDate = models.DateField()
    PasswordLastUsed = models.DateTimeField()
    ARN = models.CharField(max_length=2048,default='')
    # GroupName = models.CharField(max_length=100,default='')
    # Group_PolicyNames = models.CharField(max_length=100,default='')
    # MFA_device_name = models.CharField(max_length=100,default='')
    # MFA_device_status = models.CharField(max_length=100,default='')

    #패스워드 정책
    MinimumPasswordLength = models.IntegerField()
    RequireLowercaseCharacters = models.IntegerField()
    RequireUppercaseCharacters = models.IntegerField()
    RequireNumbers = models.IntegerField()
    RequireSymbols = models.IntegerField()
    ExpirePasswords = models.IntegerField()
    MaxPasswordAge = models.IntegerField()
    PasswordReusePrevention = models.IntegerField()
    
    
class IAMGROUPS(models.Model):
    pass
class IAMMFA(models.Model):
    pass
    # 사설 ip  = PbulicIp
    # db1 = MyResourceDetails
