from .aws_session import awsmode
import json, time,os
from pprint import pprint 

async def ec2_cmd(mode,insID,msg):
    session=await awsmode(mode)
    if(session==-1): # 인증 에러
        return -1
    ssm_cli =await session.client('ssm')
    instance_id=insID
    command=msg
    res=await ssm_cli.send_command(
            InstanceIds=[instance_id],
            DocumentName="AWS-RunShellScript",
            Parameters={"commands":[command]}
        )
    cmd_id=res['Command']['CommandId']
    # time.sleep(2) await 를 사용했기 때문에 i/o 를 기다린다
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
