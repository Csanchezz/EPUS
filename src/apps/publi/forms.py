from django import forms
from django import forms
from django.forms import ModelForm, ModelChoiceField, widgets
from apps.publi.models import *

class FormPublicacion(forms.ModelForm):
	class Meta:
		model = Publicacion
		fields = '__all__'
		widgets={
		'etiquetas': forms.SelectMultiple(attrs = {'class' : 'select2'})
		}

