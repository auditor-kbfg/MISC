from django.shortcuts import render , get_list_or_404 , redirect
from django.http import HttpResponse
from .models import AWSKEY ,EC2 ,S3DB,IAMDB, NETDB
from awssso import AWSSSO
from users.models import USERS
from .aws_session import db_session ,hard_seesion,sso_session, awsmode
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from pprint import pprint

# Create your views here.
def awskey(req):
    user=req.user
    if user.is_authenticated: # 로그인 되어있다면
        if req.method=='GET':
            return render(req,'aws/awskey.html')
        elif req.method== 'POST':
            access=req.POST.get("aws_access")
            secret=req.POST.get("aws_secret")
            token=req.POST.get("aws_token")
            region=req.POST.get("aws_region")
            profile=req.POST.get("aws_profile")
            try: 
                ret=AWSKEY.objects.get(user_id=user.username) # 조회 하여 기존 아이디를 가진 레코드 조회 후 업데이트
                ret.aws_access=access
                ret.aws_secret=secret
                ret.aws_token=token
                ret.aws_region=region
                ret.aws_profile=profile
                ret.save()
            except ObjectDoesNotExist: # 하나도 없을 때는 생성
                #  유저 조회
                ret=AWSKEY(user_id=user.username,
                            aws_access=access,
                            aws_secret=secret,
                            aws_token=token,
                            aws_region=region,
                            aws_profile=profile,fk_key=user
                        )
                ret.save()
            except:
                return redirect('/')
        else:
            return redirect('/')
        return redirect('/')
    return redirect('/users/login')
            
def awskeylist(req): #자신의 키를 볼수있는 
    if req.user.is_authenticated:
        if req.method=='GET':   
            keylist=AWSKEY.objects.filter(user_id=req.user)
            return render(req,'/aws/awskeylist.html',{'keylist':keylist})
    pass

def awskeydelete(req):
    if req.user.is_authenticated:
        keydata=AWSKEY.objects.filter(user_id=req.user.username)
        keydata.delete()
    redirect('/')

def awssso(req):
    if req.user.is_authenticated:
        if req.method=='GET':
            render(req,'/aws/ssourl.html')
        if req.method=='POST':
            LoginUrl=req.POST.get("LoginUrl")
            sso=AWSSSO()
            return redirect(sso.get_sso_login_url(LoginUrl))
    return redirect('/users/login/')


def ec2save(req):
    #  모드는 인증 
    if req.user.is_authenticated:
        mode = req.COOKIES.get('mode','1') 
        id=req.user.username
        # session=sso_session(name)
        session=awsmode(mode,id) #모드를 통해서 인증 모드는 쿠키에 있다
        cli=session.client('ec2')
        res=cli.describe_instances()
        reservation=res['Reservations'][0]
        for instance in reservation['Instances']:
            try:
                old=EC2.objects.get(InstanceId=instance['InstanceId'])
                old.PlatformDetails=instance['PlatformDetails']
                old.KeyName=instance['KeyName']
                old.InstanceType=instance['InstanceType']
                old.AvailabilityZone=instance['Placement']['AvailabilityZone']
                old.PrivateIp=instance['PrivateIpAddress']
                old.PbulicIp=instance['PublicIpAddress']
                old.PublicDns=instance['PublicDnsName']
                old.set_Tags(instance['Tags'])
                old.save()
            except ObjectDoesNotExist:
                ec2=EC2(
                    MyResourceName='test',#  이 값들은 aws에 존재 하지 않음
                    MyResourceType='server',
                    MyResourceDetails='ec2',
                    MyResourceGrade='test grade',
                    fk_key=req.user,
                    PlatformDetails=instance['PlatformDetails'],
                    InstanceId=instance['InstanceId'],
                    KeyName=instance['KeyName'],
                    InstanceType=instance['InstanceType'],
                    AvailabilityZone=instance['Placement']['AvailabilityZone'] ,# Region
                    PrivateIp=instance['PrivateIpAddress'],
                    PbulicIp=instance['PublicIpAddress'],
                    PublicDns=instance['PublicDnsName']
                    # Tags=instance['Tags'] 이녀석은 dics 배열이라 어떻레 저장 할지 고민
                )
                ec2.set_Tags(instance['Tags'])
                ec2.save()
            # pprint(instance)
        return redirect('/aws/ec2list/')
    return redirect ('/users/login')

def ec2all(req):
    ec2alldata=EC2.objects.all()
    return render(req,'aws/ec2tb.html',{'data_list':ec2alldata})

def ec2update(req):
    if req.method=='GET':
        idx=req.GET.get('id')
        ec2one=EC2.objects.get(idx=id)
        return render(req,'aws/ec2update.html',ec2one)
    elif req.method=='POST':
        ec2one=EC2.objects.get(id=id)
        return redirect('/aws/ec2list/')

def ec2detail(req):
    if req.user.is_authenticated:
        if req.method=='GET':
            idx=int(req.GET.get("id"))
            print(req.GET.get("id"))
            # ec2one=EC2.objects.get(InstanceId=id)
            ec2one=EC2.objects.get(idx=idx)
            if ec2one.fk_key==req.user: # 사용자의 것이 맞으면
                pprint(ec2one.InstanceId)
                return render(req,'aws/ec2detail.html',{'ec2one':ec2one})
    return redirect('/users/login')

def s3save(req):
    if req.user.is_authenticated:
        mode = req.COOKIES.get('mode','1') 
        id=req.user.username
        session=awsmode(mode,id) #모드를 통해서 인증 모드는 쿠키에 있다
        cli=session.client('s3')
        res=cli.describe_instances()
        reservation=res['Reservations'][0]
        for instance in reservation['Instances']:
            try:
                old=S3DB.objects.get(InstanceId=instance['InstanceId'])
                old.save()
            except ObjectDoesNotExist:
                s3db=S3DB(
                    # Tags=instance['Tags'] 이녀석은 dics 배열이라 어떻레 저장 할지 고민
                )
                s3db.set_Tags(instance['Tags'])
                s3db.save()
            # pprint(instance)
        return redirect('/aws/ec2list/')
    return redirect ('/users/login')

def s3all(req):
    if req.user.is_authenticated:
        if req.method=='GET':
            s3alldata=S3DB.objects.all()
            return render(req,'/aws/s3tb.html',{'data_list':s3alldata})
    return redirect('/users/login')

def iamsave(req):
    pass
def iamall(req):
    if req.user.is_authenticated:
        if req.method=='GET':
            iamalldata=IAMDB.objects.all()
            return render(req,'/aws/s3tb.html',{'data_list':iamalldata})
    return redirect('/users/login')

def netinfosave(req):
    pass
def netinfoall(req):
    if req.user.is_authenticated:
        if req.method=='GET':
            netalldata=NETDB.objects.all()
            return render(req,'/aws/s3tb.html',{'data_list':netalldata})
    return redirect('/users/login')















#  후에 인증 모드를 고를 수있는 api  로 이것으로 인증 방법 을 결정한다 쿠키에 넣어 사용
def session_mode(request):
    # render 함수를 사용하여 템플릿 렌더링 후, HttpResponse 객체를 생성
    response = render(request, '/')
    # HttpResponse 객체를 사용하여 쿠키를 설정
    response.set_cookie('mode', '12345') # 인증 모드를 설정하는 쿠키
    return response