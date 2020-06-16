from django.template import Library
register = Library()
@register.filter
def handle_causetype_tags(active):
    if active == 'a' :
        return '正常'
    elif active == 'b':
        return '异常'
    elif active == 'c':
        return '温度过高'
    else :
        return '损坏'