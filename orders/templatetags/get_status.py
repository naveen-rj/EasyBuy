from django import template

register = template.Library()

@register.simple_tag(name='get_status')
def get_status(status):
    status_list = ['Cart', 'Ordered', 'Under process', 'Delivered', 'Cancelled']
    return status_list[status]