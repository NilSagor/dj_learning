from django.contrib.auth import authenticate, login 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm, LoginForm

class HomePageView(TemplateView):
	template_name = 'home.html'



class ContactPageView(FormView):
	form_class = ContactForm
	template_name = 'contact/contact.html'
	success_url = '/thanks'

	def form_valid(self, form):
		return super().form_valid(form)


def LoginPageView(request):
	form = LoginForm(request.POST or None)
	# template_name = 'auth/login.html'
	# success_url = 'home.html'
	context = {
		'form': form
	}

	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			redirect('/')
			print(user)
		else:
			print("Error")
	return render(request, 'auth/login.html', context)