from clickclick.views.browsing import *
from clickclick.views.photo_management import *
from django.shortcuts import redirect, render

def home(request):
	if request.user.is_authenticated():
		return redirect('clickclick.views.photoset_list')
	else:
		return render(request, 'clickclick/home.html', {})