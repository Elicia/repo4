#encoding:utf-8
from principal.models import Receta, Comentario
from django import forms
from django.forms import ModelForm


class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo electronico')
	mensaje = forms.CharField(widget=forms.Textarea)

class RecetaForm(ModelForm):
	class Meta:
		model=Receta

class ComentarioForm(ModelForm):
	class Meta:
		model=Comentario