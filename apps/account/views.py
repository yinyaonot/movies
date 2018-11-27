from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.hashers import make_password, check_password
from itsdangerous import URLSafeSerializer
from django.core.cache import cache
from apps.account.models import User
from taopiaopiao import settings
from datetime import datetime
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.http import JsonResponse, HttpResponse


def login_view(request):
    if request.method == 'GET':
        next = request.GET.get('next')
        # 生成验证码
        key = CaptchaStore.generate_key()
        img_url = captcha_image_url(key)
        return render(request, 'account/login.html', context={'next': next, 'img_url': img_url, 'key': key})
    if request.method == 'POST':
        # 验证码的code和key
        code = request.POST.get('code')
        key = request.POST.get('key')
        img_url = captcha_image_url(key)
        # next=request.POST.get('next')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password and code:

            user = authenticate(username=username, password=password)
            # 上边只是验证用户名和密码是否正确，
            # is_active是判断用户是否是激活状态
            if user:
                # 获取对象
                cap_obj = CaptchaStore.objects.filter(hashkey=key).first()
                # 获取失效时间，与当前时间进行比较
                expiration = cap_obj.expiration
                # 获取response值
                response = cap_obj.response
                if datetime.now() < expiration and code.lower() == response:
                    # 验证码验证成功
                    if user.is_active:
                        # 登陆成功，记住登录状态
                        login(request, user)
                        return redirect('/home/movies/')
                    else:
                        return render(request, '404.html', {'msg': '你的账号未激活'})
                else:
                    # 验证失败，重新刷新验证码
                    key = CaptchaStore.generate_key()
                    img_url = captcha_image_url(key)
                    return render(request, 'account/login.html',
                                  {'img_url': img_url, 'key': key, 'capt_error': '验证码输入失败，请重新输入'})
            else:
                return render(request, 'account/login.html', {'login_msg': '账号或密码错误', 'img_url': img_url, 'key': key})
        else:
            return render(request, 'account/login.html', {'capt_error': '验证码不能为空', 'img_url': img_url, 'key': key})
    else:
        return render(request, '404.html', {'msg': '请求方式错误'})


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html')
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if username and password and phone and email and confirm_password:
                if password == confirm_password:

                    user = User.objects.all().filter(Q(username=username) | Q(phone=phone))

                    if user:
                        # 表示用户名已经存在
                        return render(request, 'account/register.html', {'username_msg': '用户已存在'})
                    else:
                        # 保存用户的操作
                        user = User.objects.create_user(username=username,
                                                        password=password,
                                                        phone=phone,
                                                        email=email,
                                                        is_active=0,
                                                        is_vip=0,
                                                        )
                        if user:
                            # login这是记住用户状态
                            # login底层做了两个操作，第一个操作将用户信息保存到session中
                            # 第二个操作将用户信息绑定到request对象中
                            # login(request, user)
                            auth_s = URLSafeSerializer(settings.SECRET_KEY, "auth")
                            token = auth_s.dumps({'name': username})
                            cache.set(token, user.id, timeout=10 * 60)
                            active_url = f'http://127.0.0.1:8000/account/active/?token={token}'
                            content = loader.render_to_string('account/mail.html',
                                                              request=request,
                                                              context={'username': username, 'active_url': active_url})
                            send_active_mail(subject='激活网站', content=content, to=[email])
                            return render(request, 'account/active_email.html')
                            # 表示用户注册成功
                        else:
                            pass
                            # 注册失败
                else:
                    return render(request, 'account/register.html', {'password_msg': '前后密码不同，注册失败'})
            else:
                return render(request, '404.html', {'msg': '请填写全部信息'})
        except Exception as e:
            return render(request, '404.html', {'msg': e})


@login_required(login_url='/account/login')
def logout_view(request):
    # 表示登出
    logout(request)
    return redirect('/home/movies/')


# @login_required(login_url='/account/login')
def update_view(request):
    try:
        if request.method == 'GET':
            return render(request, 'account/update.html')
        if request.method == 'POST':
            username = request.POST.get('username')
            user = User.objects.filter(username=username).first()
            if user:
                oldpassword = user.password
                password = request.POST.get('password')
                is_not = check_password(password, oldpassword)
                if is_not:
                    newpassword = request.POST.get('newpassword')
                    if newpassword != password:
                        user = User.objects.filter(username=username).first()
                        user.password = make_password(newpassword)
                        user.save()
                        return redirect('/account/login')
                    else:
                        return render(request, 'account/update.html', {'msg': '新密码不能与旧密码相同，修改失败'})
                else:
                    return render(request, 'account/update.html', {'msg': '原密码错误，修改失败'})
            else:
                return render(request, 'account/update.html', {'msg': '账户不存在，修改失败'})
    except Exception as e:
        return render(request, '404.html', {'msg': e})



# xxx/active/?uid=1
def active_account(request):
    token = request.GET.get('token')
    uid = cache.get(token)
    if uid:
        User.objects.filter(id=uid).update(is_active=1)
        return HttpResponse("激活成功，点击跳转到电影网站首页<a href=''>http://127.0.0.1:8000/home/movies/ </a>")
    else:
        # 激活已经失效
        # 输入邮箱或者用户名     通过用户或者邮箱查询TUser对象
        # return redirect('/')
        return render(request, '404.html', {'msg': '激活失败'})


def hello_mail(request):
    """
        subject,标题
        message, 邮件的内容
        from_email,发送邮件者
        recipient_list,  接受邮件列表
        html_message = 邮件的内容,以html格式显示邮件内容
    :param request:
    :return:
    """

    content = loader.render_to_string('account/mail.html', request=request)
    send_mail(subject='xxx线上xxx注册邮件',
              message='',
              html_message=content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=['m17538238049@163.com']
              )

    return render(request, 'account/msg.html')


def send_active_mail(subject='', content=None, to=None):
    send_mail(subject=subject,
              message='',
              html_message=content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=to
              )


# 刷新验证码
def refresh_code(request):
    key = CaptchaStore.generate_key()
    img_url = captcha_image_url(key)
    return JsonResponse({'key': key, 'img_url': img_url})
