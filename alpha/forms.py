from django import forms


class ContactForm(forms.Form):
	username = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
				'placeholder': "username"
			}))

	email = forms.CharField(
		widget = forms.EmailInput(
			attrs = {
				'class': 'form-control',
				'placeholder': "email"
			}))

	content = forms.CharField(
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control',
				'placeholder': 'write your thoughts here'
			}))


class LoginForm(forms.Form):
	username = forms.CharField(
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
				'placeholder': "username"
			}))
	password = forms.CharField(
		widget = forms.PasswordInput(
			attrs = {
				'class': 'form-control',
				'placeholder': "password"
			}))

