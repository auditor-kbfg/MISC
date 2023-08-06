from django.db import models
from users.models import USERS
import json

from web import settings
# Create your models here.
class AWSKEY(models.Model):
    idx = models.BigAutoField( primary_key=True)
    fk_key= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False,default='')
    user_id=models.CharField(max_length=50,default='')
    aws_access=models.CharField(max_length=40,default='')
    aws_secret=models.CharField(max_length=50,default='')
    aws_token=models.CharField(max_length=900,default='')
    aws_region=models.CharField(max_length=20,default='')
    aws_profile=models.CharField(max_length=40,default='')
class EC2(models.Model):
    idx=models.BigAutoField(primary_key=True)
    fk_key= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False,default='')
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
    
    # MyResourceName:str=models.CharField(max_length=20,default='test')
    # MyResourceType:str=models.CharField(max_length=10,default='server')
    # MyResourceDetails:str=models.CharField(max_length=10,default='ec2')
    # MyResourceGrade:str=models.CharField(max_length=10,default='test grade')

    """
    No    idx=models.BigAutoField(primary_key=True)
    고유 값:    fk_key= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False,default='')
    자산 이름:  MyResourceName=models.CharField(max_length=20,default='')
    자산 유형: MyResourceType=models.CharField(max_length=10,default='')
    자산 유형(상세):    MyResourceDetails=models.CharField(max_length=10,default='')
    등급(수동)    MyResourceGrade=models.CharField(max_length=10,default='')
    OS:    PlatformDetails=models.CharField(max_length=20,default='')
    자산 ID:    InstanceId=models.CharField(max_length=30,default='')
    Key 이름:    KeyName=models.CharField(max_length=20,default='')
    자산유형(t2마이크로 제거필요)    InstanceType=models.CharField(max_length=15,default='')
    지역:    AvailabilityZone=models.CharField(max_length=20,default='')
    IP(사설):    PrivateIp=models.CharField(max_length=20,default='')
    IP(공인):    PbulicIp=models.CharField(max_length=20,default='')
    DNS(공인):    PublicDns=models.CharField(max_length=100,default='')
    태그    Tags=models.TextField(default='')

    VPC(네트워크)
    SG(네트워크): 
    상태: Running/ 


    
    """

# class s3(models.Model):
#     idx = models.BigAutoField(primary_key=True)
