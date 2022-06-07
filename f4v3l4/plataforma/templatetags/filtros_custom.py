from django import template

register = template.Library()

@register.filter
def salvaContato(value):
    
    value='active'
    return value


@register.filter
def desliga_active(value):
    value='deactive'
    return value
