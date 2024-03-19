from django import template

register = template.Library()

@register.simple_tag(name='get_total')
def get_total(items):
    total = 0
    
    for item in items:
       total += item.product.price * item.quantity
    
    return total 
