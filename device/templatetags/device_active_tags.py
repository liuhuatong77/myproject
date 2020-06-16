from django.template import Library
register = Library()
@register.filter
def device_active_tags(active):
    if active == 'a' :
        return '关闭'
    else :
        return '开启'