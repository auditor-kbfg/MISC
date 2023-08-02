from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
    
class USERS(AbstractUser):
    
    def test():
        print('testuser')
    # def pwcompare(self,input_pw):
    #     if self.user_pw == input_pw:
    #         return True
    #     else:
    #         return False

    
