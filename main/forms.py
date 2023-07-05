from django import forms
from main.models import USERS

class USERSform(forms.ModelForm):
    class Meta:
        model=USERS
        fields=['user_id','user_pw']
class awskeysave(forms.ModelForm):
    class Meta:
        model=USERS
        fields=['aws_access','aws_secret','aws_token','aws_region','aws_profile']

