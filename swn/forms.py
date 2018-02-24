from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from swn.models import Planet, Notes

class UserForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, label="First Name", required=True)
	last_name = forms.CharField(max_length=30, label="Last Name", required=True)

	class Meta:
		model = User
		fields = (
			"username",
			"first_name",
			"last_name",
			"password1",
			"password2"
		)

	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.first_name = self.cleaned_data["first_name"]
		user.last_name = self.cleaned_data["last_name"]
		if commit:
			user.save()
		return user

class PlanetNotesForm(forms.ModelForm):
	class Meta:
		model=Planet
		fields = (
			"capital_and_government",
			"cultural_notes",
			"adventures_prepared",
			"party_activities_on_this_world",
		)

class NotesForm(forms.ModelForm):
	class Meta:
		model=Notes
		fields = (
			"player_notes",
			"gm_notes",
		)
