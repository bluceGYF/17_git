from django.contrib import messages
import hashlib


# post
def post(request, key):
    return request.POST.get(key, '').strip()


# post getlist
def post_list(request, key):
    return request.POST.getlist(key)


# get
def get(request, key):
    return request.GET.get(key, '').strip()


# 设置session
def set_session(request, key, value):
    request.session[key] = value


# 获取session
def get_session(request, key):
    return request.session.get(key, '')


# 删除session
def del_session(request):
    request.session.flush()


# 设置cookie
def set_cookie(response, key, value):
    response.set_cookie(key, value, max_age=60*60*24)


# 获得cookie
def get_cookie(request, key):
    return request.COOKIES.get(key, '')


# 销毁cookie
def del_cookie(response, key):
    response.delete_cookie(key)


# messages添加消息
def add_message(request, key, value):

    messages.add_message(request, messages.INFO, key + ':' + value)


# messages获得消息
def get_messages(request):

    mess = messages.get_messages(request)
    info = dict()
    for message in mess:
        content = str(message).split(':')
        info[content[0]] = content[1]

    return info


# 密码加密
def password_encryption(password, salt=''):
    sha = hashlib.sha256()
    new_password = "!@#$%" + password + salt
    sha.update(new_password.encode("utf-8"))

    return sha.hexdigest()