from channels.generic.websocket import WebsocketConsumer
from ...aws.func.funcec2cmd import *
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
    def disconnect(self, close_code):
        return super().disconnect(close_code)
    
    def receive(self, text_data=None, bytes_data=None):
        recv=json.loads(text_data)
        msg=recv['msg']
        self.send(send_data=json.dumps({
            'msg':msg
        }))
        # return super().receive(text_data, bytes_data)
    async def ec2_send(self,msg=None):
        insID=""
        mode=1
        recv=json.loads(msg)
        msg=recv['msg']
        ret= await ec2_cmd(mode,insID,msg)
        await self.send(send_data=json.dumps({
            'msg':ret
        }))
        