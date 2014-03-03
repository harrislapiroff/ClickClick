from clickclick.views.browsing import *
from clickclick.views.photo_management import *
from clickclick.views.comments import *
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render

def home(request):
	if request.user.is_authenticated():
		user_photoset_list = reverse('clickclick.user_photoset_list', args=[request.user.username])
		return redirect(user_photoset_list)
	else:
		return render(request, 'clickclick/home.html', {})