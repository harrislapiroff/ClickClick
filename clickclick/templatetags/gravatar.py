import hashlib
import urllib
from django import template

register = template.Library()


@register.simple_tag
def gravatar_url(email, size=40, default=None):
	get_vars = {'s':str(size)}
	if default:
		get_vars.update({'d':default})

	gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
	gravatar_url += urllib.urlencode(get_vars)
	return gravatar_url