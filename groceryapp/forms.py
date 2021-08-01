from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Grocery

from django import forms


# Create your forms here.
class DateInput(forms.DateInput):
    input_type = 'date'
	
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class AddGroceryForm(forms.ModelForm):

	class Meta:
		model = Grocery
		fields = '__all__'

	widgets = {
            'date': DateInput(),
        }
