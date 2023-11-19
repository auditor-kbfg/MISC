from django.shortcuts import render , get_list_or_404 , redirect
from django.http import HttpResponse ,JsonResponse
from .models import AWSKEY ,EC2 ,S3DB,IAMDB, NETDB
from .func.aws_session import db_session ,hard_seesion,sso_session, awsmode
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from pprint import pprint 
import time , json

from .func.funciam import *
from .func.funcec2 import *
from .func.funcaws import *
"""  


"""
# Create your views here.
def awskey(req):
    if req.method=='GET': # 키를 전부 지우는 로직이 있어야해
        key=getMyKey()
        # -1 이면 유저 키가 1 번을 조회 할수없음
        if(key==-1): 
            return render(req,'aws/awskey.html')
        elif(key):
            return render(req,'aws/awskey.html',{'keydata':key})
        else:
            return render(req,'aws/awskey.html')
    elif req.method== 'POST':
        access=req.POST.get("aws_access")
        secret=req.POST.get("aws_secret")
        token=req.POST.get("aws_token")
        region=req.POST.get("aws_region")
        profile=req.POST.get("aws_profile")
        ret=awsKeySave(access,secret,token,region,profile=None)
        if(ret==1 or ret ==2):
            return redirect('/')
        elif(ret==-1):
            return redirect('/')
    else:
        return redirect('/')

def awskeylist(req): #자신의 키를 볼수있는 
    if req.method=='GET':   
        keylist=AWSKEY.objects.filter(user_id=req.user)
        return render(req,'/aws/awskeylist.html',{'keylist':keylist})
    
def awskeydelete(req):
    keydata=AWSKEY.objects.filter(user_id=req.user.username)
    keydata.delete()
    return redirect('/')

def ec2save(req):
    #  모드는 인증 전부 지우고 다시 만들어
    mode = req.COOKIES.get('mode','1')
    ret=EC2save(mode)
    if(ret==-1): #세션이 이상하면 
        return redirect('/')
    elif(ret==1):
        return redirect('/aws/ec2list/')
        # pprint(instance)
    
def ec2all(req):
    ec2alldata=EC2all()
    if(ec2alldata==-1): # 만약 없다면 ec2 save 호출
        return redirect('/aws/ec2save/')
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
    if req.method=='GET':
        idx=int(req.GET.get("id"))
        print(req.GET.get("id"))
        # ec2one=EC2.objects.get(InstanceId=id)
        ec2one=EC2.objects.get(idx=idx)
        if ec2one.fk_key==req.user: # 사용자의 것이 맞으면
            pprint(ec2one.InstanceId)
            return render(req,'aws/ec2detail.html',{'ec2one':ec2one})

def s3save(req):
        mode = req.COOKIES.get('mode','1')
        id='' 
        session=awsmode(mode) #모드를 통해서 인증 모드는 쿠키에 있다
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
        return redirect('/aws/ec2list/')

def s3all(req):
        if req.method=='GET':
            s3alldata=S3DB.objects.all()
            return render(req,'/aws/s3tb.html',{'data_list':s3alldata})

def iamsave(req):
    mode = req.COOKIES.get('mode','1')
    session=awsmode(mode)
    iam_client = session.client('iam')
    # 사용자 리스트 가져오기
    user_list = iam_client.list_users()
    users = user_list['Users']    
    #패스워드 정책 가져오기
    try:
        getpasswordpolicy = iam_client.get_account_password_policy()
        password_policy = getpasswordpolicy['PasswordPolicy']
        MinimumPasswordLength = password_policy['MinimumPasswordLength']
        RequireLowercaseCharacters = password_policy['RequireLowercaseCharacters']
        RequireUppercaseCharacters = password_policy['RequireUppercaseCharacters']
        RequireNumbers = password_policy['RequireNumbers']
        RequireSymbols = password_policy['RequireSymbols']
        ExpirePasswords = password_policy['ExpirePasswords']
        MaxPasswordAge = password_policy['MaxPasswordAge']
        PasswordReusePrevention = password_policy['PasswordReusePrevention']
    except iam_client.exceptions.NoSuchEntityException:
        password_policy = ''
        MinimumPasswordLength = ''
        RequireLowercaseCharacters = ''
        RequireUppercaseCharacters = ''
        RequireNumbers = ''
        ExpirePasswords = ''
        MaxPasswordAge = ''
        PasswordReusePrevention = ''
    #IAM 사용자 정보
    for user in users:
        UserName = user['UserName']
        UserId = user['UserId']
        CreateDate = user['CreateDate']
        ARN_value = user['Arn']
        user_response = iam_client.get_user(UserName=UserName)
        pprint("user",UserId+"\n",user_response)
        try:
            PasswordLastUsed = user_response['User']['PasswordLastUsed']
        except:
            PasswordLastUsed = ""
        #MFA 정보
        try:
            mfa_response = iam_client.list_mfa_devices(UserName=UserName)
            # pprint("mfa\n",mfa_response)
            mfa_devices = mfa_response['MFADevices']
            for device in mfa_devices:
                MFA_device_name = device['SerialNumber'].split('/')[-1]
                MFA_device_status = device['DeviceStatus']
        except:
            mfa_devices = ""
        # 사용자가 소속된 그룹 가져오기
        try:
            groups_response = iam_client.list_groups_for_user(UserName=user)
            # pprint("groups\n",groups_response)
            groups = groups_response['Groups'] 
            for group in groups:
                GroupName = group['GroupName']
                # 그룹의 인라인 정책 가져오기
                group_inline_policies = iam_client.list_group_policies(GroupName=GroupName)
                # pprint("group inline polices",group_inline_policies)
                Group_PolicyNames = group_inline_policies['PolicyNames']
        except:
            GroupName = ""
        iamdata=IAMDB(
            UserName = UserName,
            UserId = UserId,
            CreateDate = CreateDate,
            PasswordLastUsed =PasswordLastUsed,
            ARN = ARN_value,
            MinimumPasswordLength = MinimumPasswordLength,
            RequireLowercaseCharacters = RequireLowercaseCharacters,
            RequireUppercaseCharacters = RequireUppercaseCharacters,
            RequireNumbers = RequireNumbers,
            RequireSymbols = RequireSymbols,
            ExpirePasswords =ExpirePasswords,
            MaxPasswordAge = MaxPasswordAge,
            PasswordReusePrevention = PasswordReusePrevention
        )
        iamdata.save()
        pprint()
    
    return redirect('/')

def iamall(req):
        if req.method=='GET':
            iamalldata=IAMDB.objects.all()
            return render(req,'aws/s3tb.html',{'data_list':iamalldata})
def netinfosave(req):
    pass
def netinfoall(req):
        if req.method=='GET':
            netalldata=NETDB.objects.all()
            return render(req,'aws/s3tb.html',{'data_list':netalldata})

# async  를 사용해서 다른 함수도 await 를 사용해야지 문제 없이 작동함
async def instance_cmd(req): 
    if req.method=='GET':
        instance_id= req.GET.get("Instance_Id")
        if(instance_id==""):
            return redirect('/')
        server_ip=req.GET.get("Public_Ip")
        res=render(req,'aws/ec2cmd.html')
        # print('dsfdsf')
        # 쿠키에 서버 정보를 삽입
        res.set_cookie('Public_Ip',server_ip)
        res.set_cookie('Instance_ID',instance_id)
        return res
    if req.method=='POST':
        mode = req.COOKIES.get('mode','1')
        instance_id=req.COOKIES.get("Instance_ID",'')
        session=awsmode(mode)
        if(session==-1):
            return redirect('/')
        ssm_cli =session.client('ssm')
        try: # 제대로 파싱 하지 못하면 에러를 리턴
            getData=json.loads(req.body)
            command=getData['command']
        except json.JSONDecodeError as err:
            return JsonResponse(err)
        # pprint(command)
        # retData={"data":command+"  server add data"}
        # return JsonResponse(retData)
        res=ssm_cli.send_command(
            InstanceIds=[instance_id],
            DocumentName="AWS-RunShellScript",
            Parameters={"commands":[command]}
        )
        cmd_id=res['Command']['CommandId']
        time.sleep(2)
        while True:
            result= await ssm_cli.get_command_invocation(
                InstanceId=instance_id,
                CommandId=cmd_id,
            )
            if result['Status'] in ('Success','Failed','Cancelled'):
                output=result.get('StandardOutputContent','Command exqution failed or was canceled.')
                break
        # return JsonResponse(result) # json만을 응답값으로 준다
        pprint("ret",result)
        pprint("out",output)
        return JsonResponse(cmd_id)

def ssmgroup(req):
    if req.method=="POST":
        # AWS 자격 증명 설정
        mode = req.COOKIES.get('mode','1')
        session=awsmode(mode)
        if(session==-1):
            return redirect('/')
        iam_client=session.client("iam")
        # 그룹 을 생성 해서
        group_name = 'cspmSSMFullAcess'
        iam_client.create_group(GroupName=group_name)

        # 정책 ARN (SSM Full Access 정책 ARN) 가져오기
        ssm_full_access_policy_arn = 'arn:aws:iam::aws:policy/AmazonSSMFullAccess'

        # 그룹에 정책 부여
        iam_client.attach_group_policy(GroupName=group_name, PolicyArn=ssm_full_access_policy_arn)

        print(f'그룹 {group_name}이 생성되었고, SSM Full Access 권한이 부여되었습니다.')
    # 성공시 실패시 결과 다르게 반환
#ssm 이있는지 
#그룹 만들고 현재 사용자 넣기



#  후에 인증 모드를 고를 수있는 api  로 이것으로 인증 방법 을 결정한다 쿠키에 넣어 사용
def session_mode(request):
    # render 함수를 사용하여 템플릿 렌더링 후, HttpResponse 객체를 생성
    response = render(request, '/')
    # HttpResponse 객체를 사용하여 쿠키를 설정
    response.set_cookie('mode', '12345') # 인증 모드를 설정하는 쿠키
    return response