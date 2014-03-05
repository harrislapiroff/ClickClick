from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView

from clickclick.forms import UserUpdateForm


def login(request, *args, **kwargs):
	return auth_views.login(request, template_name="clickclick/auth/login.html", *args, **kwargs)


@login_required
def password_change(request, *args, **kwargs):
	return auth_views.password_change(request, template_name="clickclick/auth/password_change.html", post_change_redirect='/', *args, **kwargs)


class UserUpdateView(UpdateView):
	template_name = "clickclick/auth/user_update.html"
	form_class = UserUpdateForm

	def get_success_url(self):
		return "/"

	def get_object(self):
		if self.request.user.is_authenticated():
			return self.request.user
		else:
			return None


user_update = UserUpdateView.as_view()
