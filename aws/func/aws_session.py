import boto3
# from dotenv import load_dotenv
import os
from ..models import AWSKEY

# .env 를 이용한
def env_session():
    aws_access=os.environ.get('aws_access_key_id')
    aws_secret=os.environ.get('aws_secret_access_key')
    aws_token=os.environ.get('aws_session_token')
    aws_region=os.environ.get('region_name')
    session=boto3.Session(
        aws_access_key_id=aws_access,
        aws_secret_access_key=aws_secret,
        aws_session_token=aws_token,
        region_name=aws_region
    )
    return session
# db에서 id 를 기준으로 값을 뽑아서 연결 
def db_session():
    key= AWSKEY.objects.get(idx=1)
    session = boto3.Session(
        aws_access_key_id=key.aws_access,
        aws_secret_access_key=key.aws_secret,
        aws_session_token=key.aws_token,
        region_name=key.aws_region,
    )
    print('db session ')
    return session
def hard_seesion():
    print('hard session')
    session=boto3.Session(
        aws_access_key_id="",
        aws_secret_access_key="",
        aws_session_token="",
        region_name="ap-northeast-2"
    )
    print(session)
    return session
# db 에있는 profile을 이용한 연결
def profile_session(id):
    profile=AWSKEY.objects.get(user_id=id)
    session=boto3.Session(aws_profile=profile.aws_profile)
    return session
def base_session():
    session=boto3.Session()
    return session
def sso_session(name:str):
    session=boto3.Session(profile_name=name)
    return session

# class aws_session():
# 인증모드에 따라서 인증함
def awsmode(num:str): # 기본값 db session
    session=None
    try:
        if num=='1':
            session=db_session()
        elif num=='2':
            session=hard_seesion()
        elif num=='3':
            session=env_session()
        elif num=='4':
            session=base_session()
        elif num=='5':
            session=sso_session('vanni')
        return session
    except:
        return -1