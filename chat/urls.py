from django.urls import path
from . import views
"""  """
urlpatterns = [
    path('', views.index),
    path('ec2cmd/',views.chat_cmd),
    
]