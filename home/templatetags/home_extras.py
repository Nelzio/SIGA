from django import template

register = template.Library()


@register.filter
def first_word(value):
    list_value = value.split(" ")
    val = ""
    for v in list_value:
        if v != v.lower():
            val = val + v[0]
    return val


@register.filter
def spacing_no(value):
    list_value = value.split(" ")
    val = ""
    for v in list_value:
        val = val + v
    return val
