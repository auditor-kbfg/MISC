from django.shortcuts import render, redirect
from .models import AWSKEY
from .aws_session import db_session, hard_seesion
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

import boto3

# Create your views here.
def awskey(req):
    if req.method == 'POST':
        id = req.POST.get("user_id")
        access = req.POST.get("aws_access")
        secret = req.POST.get("aws_secret")
        token = req.POST.get("aws_token")
        region = req.POST.get("aws_region")
        profile = req.POST.get("aws_profile")

        if any(value is None for value in [id, access, secret, token, region, profile]):
            return HttpResponse("입력값이 누락되었습니다")

        try: 
            ret = AWSKEY.objects.get(user_id=id) # 조회하여 기존 아이디를 가진 레코드 조회 후 업데이트
            ret.aws_access = access
            ret.aws_secret = secret
            ret.aws_token = token
            ret.aws_region = region
            ret.aws_profile = profile
            ret.save()
        except ObjectDoesNotExist: # 하나도 없을 때는 생성
            ret = AWSKEY(user_id=id, aws_access=access, aws_secret=secret, aws_token=token, aws_region=region, aws_profile=profile)
            ret.save()
        except:
            return redirect('/')
        return redirect('/')
    else: # GET 
        return render(req, 'aws/awskey.html')
    
def resource(req):
    if req.method=='POST':
        id=req.POST.get("user_id")
        print(id)
        session=db_session(id)
        print("session",session)
        user=session.client('sts')
        account_id =user.get_caller_identity().get('Account')
        print("3",account_id)
        return redirect('/')
    else:
        return render(req,'aws/resource.html')
def ec2(req):
    if req.method=='POST':
        id=req.POST.get('user_id')
        session=db_session(id)
        ec2=session.client('ec2')
        ec2_info={}
        ret=ec2.describe_instances()
        for reservation in ret["Reservations"]:
            for i in reservation["Instances"]:
                for j in i['Tags']:
                    tagName='None'
                    if j['Key']== 'Name':
                        tagName=j['Value']
                ec2_info[i["InstanceId"]]=[tagName,i['InstanceType'],i['State']['Name']]
        print(ec2_info)
        return redirect('/')
    else:
        return redirect('/')
    