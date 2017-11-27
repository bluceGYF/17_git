from django.shortcuts import render
import random
from django.http import HttpResponse
from .functions import *
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import JsonResponse


@check_permission
def vip(request):
    # 省市联动
    cities = CityInfo.objects.filter(city_baba=None)
    username = get_session(request, 'username')
    user = User.objects.user_by_user_name(username)
    mess = get_messages(request)
    return render(request, 'user/vip.html', locals())


# 用户中心省市联动ajax提交视图
def city_change(request):
    baba_code = get(request, 'baba_code')
    cities = CityInfo.objects.filter(city_baba=baba_code)
    city_list = []
    for city in cities:
        info = dict()
        info['name'] = city.city_name
        info['code'] = city.city_code
        city_list.append(info)
    return JsonResponse({'ret': city_list})


@check_permission
def vip_adress(request):
    return render(request, 'user/vip_adress.html', locals())


@check_permission
def use_detail(request):
    return render(request, 'user/use_detail.html', locals())


@check_permission
def info(request):
    return render(request, 'user/info.html', locals())


@check_permission
def uorder(request):
    return render(request, 'user/uorder.html', locals())


def repwd(request):
    return render(request, 'user/repwd.html', locals())


@check_permission
def state(request):
    return render(request, 'user/state.html', locals())


def login(request):
    mess = get_messages(request)
    return render(request, 'user/login.html', locals())


def reg(request):
    mess = get_messages(request)
    return render(request, 'user/reg.html', locals())


# 检测用户名是否存在
def check_username(request):
    if user_is_exist(request):
        return JsonResponse({'ret': 1})
    else:
        return JsonResponse({'ret': 0})


@check_permission
def message(request):
    return render(request, 'user/message.html', locals())


# ----------------------注册模块验证码-------------------------
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO


# 绘制随机字符
def generate_random_string(request):
    # 随机字符串
    chars = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 随机产生４个不同字符
    random_chars = "".join(random.sample(chars, 4))
    # 随机字符存储到session中
    request.session['verify_code'] = random_chars

    return random_chars


# 获得图片背景颜色
def draw_disturb_point(pen_for_image):
    for _ in range(100):
        # 随机生成干扰点位置
        pos = (random.randint(0, 100), random.randint(0, 30))
        # 随机生成点的颜色
        color = (random.randint(0, 255), 255, random.randint(0, 255))
        # 将点绘制到图片上
        pen_for_image.point(pos, color)


# 给图片绘制随机文字
def draw_random_string(pen_for_image, random_string):
    # 加载字体 字体所在目录:/usr/share/fonts/
    my_font = ImageFont.truetype('FreeMono.ttf', 23)
    # 设置字符颜色
    my_color = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制字符
    for number, ch in enumerate(random_string):
        pen_for_image.text((5 + number * 20, 2), ch, my_color, my_font)


# 绘制基本图片
def create_base_image():
    # 定义图片背景颜色(RGB)
    bg_color = (random.randrange(20, 100), random.randrange(20, 100), 255)
    # 创建图片, 分别设置图片格式, 图片大小, 图片背景颜色
    verify_image = Image.new('RGB', (100, 30), bg_color)

    return verify_image


# 随机图片视图函数
def verification_code(request):
    # 生成随机字符序列
    random_string = generate_random_string(request)
    # 创建图片对象
    verify_image = create_base_image()
    # 创建对图片(verify_image)的画笔
    pen_for_image = ImageDraw.Draw(verify_image)
    # 将随机字符绘制到图片上
    draw_random_string(pen_for_image, random_string)
    # 绘制图片干扰点
    draw_disturb_point(pen_for_image)

    # 将图片数据暂存到内存中
    image_data = BytesIO()
    verify_image.save(image_data, 'png')

    return HttpResponse(image_data.getvalue(), 'image/png')


# --------------------------处理用户注册----------------------------------
def register_handle(request):
    # 如果参数校验合法
    if check_register_params(request):
        # 注册数据入库
        try:
            User.objects.user_register_save(request)
            # flag = 1
            # 跳转到登录页面
            add_message(request, 'flag', '1')
            return redirect(reverse('user:login'))
        except:
            # flag = 0
            # 跳转到注册页面
            add_message(request, 'flag', '0')
            return redirect(reverse('user:reg'))
    # 如果校验不合法
    else:
        # flag = 0
        # 跳转到注册页面
        add_message(request, 'flag', '0')
        return redirect(reverse('user:reg'))


def check_yanzheng(request):
    yanzheng = get(request, 'yanzheng')

    if not yanzheng == str.lower(get_session(request, 'verify_code')):
        return JsonResponse({'ret': 0})
    return JsonResponse({'ret': 1})


# ----------------处理用户登陆--------------------
def login_handle(request):
    # 检测用户登陆是否成功
    if check_login_params(request):
        # 保持用户登陆状态
        #checkbox = get(request, 'check_box')
        # print(checkbox)
        keep_user_online(request)
        # 暂时跳转到用户中心(跳转到登陆前的页面)
        url = get_redirect_url(request)
        print('1---------121----:', get_session(request, 'pre_url'))
        return redirect(url)
    # 如果登陆失败
    else:
        return redirect(reverse('user:login'))


def logout_handle(request):
    del_session(request)
    return redirect(reverse('user:login'))


# 修改地址
def user_edit_addr(request):
    if user_is_login(request):
        # 如果参数合格
        if check_addr_edit_params(request):
            user_addr = get_user_addr(request)
            add_message(request, 'edit_addr', 'true')
            User.objects.user_addr_updata(request, user_addr)
        else:
            add_message(request, 'edit_addr', 'false')
        return redirect(reverse('user:vip'))


