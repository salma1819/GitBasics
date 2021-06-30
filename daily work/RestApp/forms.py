#from django.forms import ModelForm
from RestApp.models import Restaurant
from django import forms

class ReForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ["Rname","Nitems","timings","address"]
		widgets = {
		"Rname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Restaurant Name",
			}),
		"Nitems":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Number of Items available in Resturant",
			}),
		"timings":forms.TimeInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter timings",
			"type":"time",
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Address",
			"rows":2,
			}),

		}