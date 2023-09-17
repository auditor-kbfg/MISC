from .aws_session import  awsmode
from ..models import AWSKEY
from django.core.exceptions import ObjectDoesNotExist

def getMyKey():
    ret=AWSKEY.objects.get(idx=1)
    return ret

def awsKeySave(access,secret,token,region,profile):
    try: # 과연 하나만 쓰는가?
        ret=AWSKEY.objects.get(idx=1) # 조회 하여 기존 아이디를 가진 레코드 조회 후 업데이트
        ret.aws_access=access
        ret.aws_secret=secret
        ret.aws_token=token
        ret.aws_region=region
        if profile is not None: #profile None 이 아니면 할당 
            ret.aws_profile=profile
        ret.save()
        return 2
    except ObjectDoesNotExist: # 하나도 없을 때는 생성
        ret=AWSKEY(
                    aws_access=access,
                    aws_secret=secret,
                    aws_token=token,
                    aws_region=region,
                    aws_profile=profile,
                )
        ret.save()
        return 1
    except:
        return -1
    