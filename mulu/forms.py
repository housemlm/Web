from django import forms
from mulu.models import furniture

class FurnitureDetails (forms.ModelForm):
	details = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
	class Meta:
		model = furniture
		fields = {'title','pic'}

	    
	


