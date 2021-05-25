from django.shortcuts import render
from .forms import StudentForm
from .db import update_user_info

def index(request):

	form = StudentForm()

	if request.method == 'POST' and form.is_valid():
		form = StudentForm(request.POST)
		form.save()
			
	context = {'form':form}
	return render(request, 'app/index.html', context)