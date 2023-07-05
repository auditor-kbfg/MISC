from django.urls import path

from . import views


urlpatterns = [
    path('awskey/',views.awskey),
    path('resource/',views.resource),
    path('ec2/',views.ec2),
]