from math import floor

from django import template

register = template.Library()


@register.filter(name='convert_minutes')
def convert_minutes(value):
    hours = floor(value / 60)
    minutes = value - (hours * 60)
    return f'{hours:02d}:{minutes:02d}'
