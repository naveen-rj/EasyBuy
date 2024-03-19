from django import template

register = template.Library()

@register.simple_tag(name='add')
def add(a, b):
    return a + b