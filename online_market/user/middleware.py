from django.core.urlresolvers import reverse
import re
from utils.wrappers import *


# 记录用户访问地址
class RecordUrlMiddleware(object):
    def process_response(self, request, response):

        # 不记录url的页面
        exclude_urls = [
            reverse('user:vip'),
            reverse('user:vip_adress'),
            reverse('user:use_detail'),
            reverse('user:info'),
            reverse('user:uorder'),
            reverse('user:repwd'),
            reverse('user:state'),
            reverse('user:login'),
            reverse('user:logout_handle'),
            reverse('user:reg'),
            reverse('user:message'),
            reverse('user:check_username'),
            reverse('user:login_handle'),
            reverse('user:register_handle'),
            reverse('user:check_yanzheng'),
        ]
        if not re.match(r'^/user/verification_code/\d+/$', request.path):
            # print(request.path)
            # print('pre_url===============:', re.match(r'^/user/verification_code/\d+/$', request.path))
            if request.path not in exclude_urls and response.status_code == 200:
                # request.session['pre_url'] = request.get_full_path()
                set_cookie(response, 'pre_url', request.get_full_path())

            return response


