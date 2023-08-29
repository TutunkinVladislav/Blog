from math import floor

from django import template

register = template.Library()


@register.filter(name='convert_minutes')
def convert_minutes(value):
    hours = floor(value / 60)
    minutes = value - (hours * 60)
    return f'{hours:02d}:{minutes:02d}'


@register.filter(name='declenation_comment')
def declenation_comment(count):
    value = ('комментарий', 'комментария', 'комментариев')
    keys = (2, 0, 1, 1, 1, 2)
    if count == '':
        return ''
    mod = count % 100
    print(mod)
    if 9 < mod < 20:
        value_key = 2
    else:
        value_key = keys[min(mod % 10, 5)]
    return value[value_key]
