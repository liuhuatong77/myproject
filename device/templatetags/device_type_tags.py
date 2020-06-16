from django.template import Library
register = Library()
@register.filter
def device_type_tags(type):
    if type == 'a':
        return '正常'
    elif type == 'b':
        return '异常'
    elif type == 'c':
        return '温度过高'
    else :
        return '损坏'