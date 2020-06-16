#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import random

def duanxin(telephone):
    client = AcsClient('LTAI4FvQou3xqP1WA96rPEpA', 'BdwA6BY0oJOx3EB4gltWPrGKkkbVZf', 'cn-hangzhou')
    s=''
    for i in range(4):
        s+=str(random.randint(0,9))
    message = "{"+"code:"+s+"}"
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', telephone)
    request.add_query_param('SignName', "生鲜电商注册验证码")
    request.add_query_param('TemplateCode', "SMS_193240537")
    request.add_query_param('TemplateParam', message)

    response = client.do_action(request)
    # python2:  print(response)
    print(str(response, encoding = 'utf-8'))
