from django.urls import path

from . import views


urlpatterns = [
    path('awskey/',views.awskey),
    path('ec2save/',views.ec2save),
    path('ec2list/',views.ec2all),
    path('ec2detail/',views.ec2detail),
    path('s3save/',views.s3save),
    path('s3all/',views.s3all),
    path('netinfosave/',views.netinfosave),
    path('netinfoall/',views.netinfoall),
    path('awssso/',views.awssso),
] 