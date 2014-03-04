from django.contrib.auth.views import login as auth_login

def login(request, *args, **kwargs):
	return auth_login(request, template_name="clickclick/auth/login.html", *args, **kwargs)