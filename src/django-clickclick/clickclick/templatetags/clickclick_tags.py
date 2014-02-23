from django import template
from clickclick.settings import CLICKCLICK_TITLE

register = template.Library()

@register.simple_tag
def clickclick_title():
	return CLICKCLICK_TITLE