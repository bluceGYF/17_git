from utils.wrappers import *
import re
from .models import *
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


def check_register_params(request):
    user_name = post(request, 'user_name')
    user_pass1 = post(request, 'pass1')
    user_pass2 = post(request, 'pass2')
    user_yz = post(request, 'yanzhen')
    user_xieyi = post(request, 'user_xieyi')
    # 如果错误提交 勾选框的处理
    if user_xieyi == '1':
        check = ''
    else:
        check = '1'
    flag = True
    # 判断用户名是否合法
    if not re.match('^[A-Za-z0-9]{8,16}$', user_name):
        add_message(request, 'user_name', '用户名为8到16位字母或者数字')
        add_message(request, 'user_name_val', user_name)
        flag = False
    if not re.match('^[A-Za-z0-9]{6,12}$', user_pass1):
        add_message(request, 'user_pass1', '密码为6到12位字母或数字')
        add_message(request, 'user_pass1_val', user_pass1)
        flag = False
    if user_pass1 != user_pass2:
        add_message(request, 'user_pass2', '两次密码不一致')
        add_message(request, 'user_pass2_val', user_pass2)
        flag = False
    if not (user_yz == str.lower(get_session(request, 'verify_code'))):
        add_message(request, 'user_yz', '验证码不正确')
        add_message(request, 'user_yz_val', user_yz)
        flag = False
    if not user_xieyi == '1':
        add_message(request, 'user_xieyi', '必须同意协议')
        add_message(request, 'user_check', check)
        flag = False
    return flag


# 检测用户名是否存在
def user_is_exist(request):
    # 获得用户名
    username = get(request, 'username')
    return User.objects.user_by_user_name(username)


# 检测用户登陆参数
def check_login_params(request):

    # 获得表单用户名和密码和是否保持登陆状态
    username = get(request, 'user_name')
    password = get(request, 'pass_word')

    # 先判断输入的用户名和密码是否符合基本规范
    if not re.match('^[A-Za-z0-9]{8,16}$', username):
        # print('1-------------:', username)
        add_message(request, 'flag_login', '0')
        return False
    if not re.match('^[A-Za-z0-9]{6,12}$', password):
        # print('2-------------')
        add_message(request, 'flag_login', '0')
        return False
    # 符合基本规范，查数据库是否匹配
    user = User.objects.user_by_user_name(username)
    # 如果用户存在
    if user:
        # 判断密码
        if user.user_pass == password_encryption(password):
            return True
        else:
            add_message(request, 'flag_login', '0')
            return False
    # 如果用户不存在
    else:
        add_message(request, 'flag_login', '0')
        return False


# 保持用户登陆状态
def keep_user_online(request):
    checkbox = get(request, 'check_box')
    username = get(request, 'user_name')
    user = User.objects.get(user_name=username)
    uid = user.id
    if checkbox == 'on':
        set_session(request, 'username', username)
        set_session(request, 'uid', uid)
    else:
        set_session(request, 'username', username)
        request.session.set_expiry(0)


# 获得要重定向的页面
def get_redirect_url(request):
    url = get_cookie(request, 'pre_url')
    if url:
        return url
    else:
        return reverse('goods:index')


# 判断用户是否已经登陆
def user_is_login(request):
    return get_session(request, 'username')


# 用户权限验证装饰器
def check_permission(view_func):
    def wrapper(request, *args, **kwargs):
        # 检测用户是否登陆
        if user_is_login(request):
            return view_func(request, *args, **kwargs)
        # 如果没有登陆，返回登陆页面
        else:
            return redirect(reverse('user:login'))
    return wrapper


# 检测用户修改地址参数
def check_addr_edit_params(request):
    user_card_id = post(request, 'id_card')
    user_code = post(request, 'code')
    user_cellphone = post(request, 'cell_phone')
    user_tele = post(request, 'tele')
    user_true_name = post(request, 'true_name')
    user_addr = post(request, 'user_detail_addr')
    user_c1 = post(request, 'c1')
    user_c2 = post(request, 'c2')
    user_c3 = post(request, 'c3')
    if user_true_name == '':
        print('1------------')
        return False
    if len(user_card_id) != 18:
        print('2------------')
        return False
    if len(user_code) != 6:
        print('3------------')
        return False
    if len(user_cellphone) != 11:
        print('4------------')
        return False
    if len(user_tele) != 12:
        print('5------------')
        return False
    if user_c1 == '请选择省':
        print('6------------')
        return False
    if user_c2 == '请选择市':
        print('7------------')
        return False
    if user_c3 == '请选择地区':
        print('8------------')
        return False
    if user_addr == '':
        print('9------------')
        return False
    return True


def get_user_addr(request):
        c1 = post(request, 'c1')
        province = CityInfo.objects.get(city_code=c1)
        pr_name = province.city_name
        # print(pr_name)
        c2 = post(request, 'c2')
        city = CityInfo.objects.get(city_code=c2)
        city_name = city.city_name
        # print(city_name)
        c3 = post(request, 'c3')
        area = CityInfo.objects.get(city_code=c3)
        area_name = area.city_name
        # print(area_name)
        user_addr = pr_name + city_name + area_name
        return user_addr



