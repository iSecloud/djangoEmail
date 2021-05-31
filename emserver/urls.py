from django.urls import path
from . import views

#路由
app_name = 'emserver' #声明一个命名空间

urlpatterns = [
    path('', views.send_email, name='index'),

]