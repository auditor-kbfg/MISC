from ..models import EC2
from .aws_session import awsmode

# update ec2 다시 저장시 db와 aws 비교 같이 존재하는것은 달라진것 있으면 수정
# db 에만 있는것은 삭제 , aws 에만 있는것은 추가 하는 로직 필요

def EC2save(mode):
    session=awsmode(mode) #모드를 통해서 인증 모드는 쿠키에 있다
    if(session==-1):
        return -1
    # session=db_session()
    cli=session.client('ec2')
    res=cli.describe_instances()
    reservation=res['Reservations'][0]
    for instance in reservation['Instances']:
        de=EC2.objects.all().delete() #전부 지우고
        ec2=EC2(
            MyResourceName='res name',#이 값들은 aws에 존재 하지 않음
            MyResourceType='server',
            MyResourceDetails='EC2',
            MyResourceGrade='grade',
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
    return 1
def EC2all():
    ret=EC2.objects.all()
    if(ret):
        return ret
    return -1
    