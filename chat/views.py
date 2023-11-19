from django.shortcuts import render , redirect

# Create your views here.
def index(req):
    return render(req,'chat/index.html',{})

# def room(req, room_name):
    # return render(request, 'chat/room.html', {'data': data})

def chat_cmd(req): 
    if req.method=='GET':
        instance_id= req.GET.get("Instance_Id")
        mode = req.COOKIES.get('mode','1')
        if(instance_id==""):
            return redirect('/')
        server_ip=req.GET.get("Public_Ip")
        ret={
            'InsId':instance_id,
            'mode':mode,
            'ServerIp':server_ip
        } 
        # 쿠키에 서버 정보를 삽입
        # res.set_cookie('Public_Ip',server_ip)
        # res.set_cookie('Instance_ID',instance_id)
        return render(req,'chat/chatcmd.html',{"data":ret})