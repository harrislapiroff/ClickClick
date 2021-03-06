from django.forms import ModelForm
from django.contrib.auth.models import User

class UserUpdateForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')
