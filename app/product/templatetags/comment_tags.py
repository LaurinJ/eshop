from django import template

register = template.Library()

@register.filter
def stars(obj):
    return range(1,6)