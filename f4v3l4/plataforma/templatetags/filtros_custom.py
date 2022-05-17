from django import template

register = template.Library()

@register.filter
def liga_active(value):
    value='active'
    return value


@register.filter
def desliga_active(value):
    value='deactive'
    return value
