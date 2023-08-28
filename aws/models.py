from django.db import models
from users.models import USERS
import json

from web import settings
# Create your models here.
class AWSKEY(models.Model):
    # idx = models.BigAutoField( primary_key=True)
    idx = models.IntegerField( primary_key=True,default=1)
    # fk_key= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False,default='')
    # user_id=models.CharField(max_length=50,default='')
    aws_access=models.CharField(max_length=40,default='')
    aws_secret=models.CharField(max_length=50,default='')
    aws_token=models.CharField(max_length=900,default='')
    aws_region=models.CharField(max_length=20,default='')
    aws_profile=models.CharField(max_length=40,default='')
class EC2(models.Model):
    idx=models.BigAutoField(primary_key=True)
    # fk_key= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False,default='')
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
    # 사설 ip  = PbulicIp
    # db1 = MyResourceDetails
    
    # MyResourceName:str=models.CharField(max_length=20,default='test')
    # MyResourceType:str=models.CharField(max_length=10,default='server')
    # MyResourceDetails:str=models.CharField(max_length=10,default='ec2')
    # MyResourceGrade:str=models.CharField(max_length=10,default='test grade')

# class s3(models.Model):
#     idx = models.BigAutoField(primary_key=True)
