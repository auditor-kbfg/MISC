import json
from channels.generic.websocket import AsyncWebsocketConsumer
from aws.func.funcec2cmd import ec2_cmd

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.username="ec2"
        print("connect",1)
        await self.accept()      
    async def disconnect(self, close_code):
        pass
        await self.send(text_data=json.dumps({
            'state':"0",
            'msg':"socket disconect"
        }))
        # pass
        # print(2)
        return super().disconnect(close_code)
    
    async def receive(self, text_data=None, bytes_data=None):
        recv=json.loads(text_data)
        # 인스 턴스 아이디 와 인증모드 
        InsId=recv['InsId']
        mode=recv['mode']
        msg=recv['msg'] 
        # 대충 여기에서 명령어 실행 함수 ㄱㄱ
        cmdret=await ec2_cmd(msg)
        if(msg==""):
            await self.send(text_data=json.dumps({
                'msg':"내용 없음"
            }))
        await self.send(text_data=json.dumps({
            'msg':msg
        }))
        
        
        
        # return super().receive(text_data, bytes_data)
    # async def ec2_send(self,msg=None):
    #     recv=json.loads(msg)
    #     InsID=recv['InsId']
    #     mode=recv['mode']
    #     msg=recv['msg']
    #     print(InsID,mode,msg)
    #     if type(mode)==int:
    #         print(mode ,"int",)
    #     # ret= await ec2_cmd(mode,insID,msg)
    #     ret="test"
    #     await self.send(send_data=json.dumps({
    #         'msg':ret
    #     }))
        