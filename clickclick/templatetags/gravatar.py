import hashlib
import urllib
from django import template

register = template.Library()


@register.simple_tag
def gravatar_url(email, size=40, default="blank", rating="g"):
	parameters = {
		's': str(size),
		'd': default,
		'r': rating,
	}

	gravatar_url = "//www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
	gravatar_url += urllib.urlencode(parameters)
	return gravatar_url