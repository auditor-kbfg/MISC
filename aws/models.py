from django.db import models
# Create your models here.
class AWSKEY(models.Model):
    idx = models.BigAutoField( primary_key=True)
    # fk_key= models.ForeignKey(USERS, on_delete=models.CASCADE)
    user_id=models.CharField(max_length=50)
    aws_access=models.CharField(max_length=40)
    aws_secret=models.CharField(max_length=50)
    aws_token=models.CharField(max_length=900)
    aws_region=models.CharField(max_length=20)
    aws_profile=models.CharField(max_length=40)
