import re

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MymiddleWare(MiddlewareMixin):
    def process_request(self,request):
        print('--My process request--')

    def process_view(self,request,callback,callback_args,callback_kwargs):
        print('--My process view--')

    def process_response(self,request,reponse):
        print('--My process response--')
        # 必须有response
        return reponse

class VisitLimit(MiddlewareMixin):
    visit_times = {}
    def process_request(self,request):
        ip_address = request.META.get('REMOTE_ADDR')
        if re.match('^/test/$',request.path_info):
            time = self.visit_times.get(ip_address,0)
            self.visit_times[ip_address] =  time + 1
            if time >5:
                return HttpResponse('你已经访问过'+ str(time) + '次,您被禁止了')
        return