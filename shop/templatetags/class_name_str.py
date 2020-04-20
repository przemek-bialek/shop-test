from django import template


register = template.Library()
@register.filter
def class_name_str(instance):
    return instance.__class__.__name__
