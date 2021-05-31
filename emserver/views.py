from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.shortcuts import HttpResponse

def send_email(request):
    send_mail(
        subject='django邮件服务',
        message='有人登陆了这个网站',
        from_email='869820505@qq.com',  # 发件人
        recipient_list=['3361371063@qq.com'],  # 收件人
        #收件人可以直接写，也可以从setting.py中配置中导入
        fail_silently=False
    )
    return HttpResponse('邮件服务测试成功')