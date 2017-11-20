from django import template

register=template.Library()
@register.filter
def set_name(l):
	return l[0]