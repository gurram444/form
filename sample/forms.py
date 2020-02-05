from .models import *
from django import forms


# Create your views here


class Form1(forms.ModelForm):
	class Meta:
		model = Model1
		fields='__all__'

class Form2(forms.ModelForm):
	class Meta:
		model = Model2
		fields='__all__'

class Form3(forms.ModelForm):
	class Meta:
		model=Model3
		fields='__all__'

