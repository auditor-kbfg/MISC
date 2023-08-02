from django.shortcuts import render , get_list_or_404 , redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(req):
    return render(req,'main/index.html')

@csrf_exempt
def reqtest(req):
    if req.method =='POST':
        a=req.POST.get("id")
        print("post")
        print(a)
        return redirect('/')
    else:
        # a=id
        a=req.GET.get('id')
        print("get")
        print(a)
        return redirect('/')
def modetest(req):
    mode=req.COOKIES.get('mode')
    print(mode)
    print(type(mode))
    return redirect('/')