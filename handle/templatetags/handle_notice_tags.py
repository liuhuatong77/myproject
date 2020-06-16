from django.template import Library
register = Library()
@register.filter
def handle_notice_tags(active):
    if active == 'a' :
        return '不通知'
    elif active == 'b':
        return '弹窗警告'
    elif active == 'c':
        return '邮箱通知'
    else :
        return '短信通知'