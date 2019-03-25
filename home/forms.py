from django.forms.widgets import ClearableFileInput
from django.forms import widgets
from django import forms
from .models import Contacto, Endereco, Estudante


class ContactoModelForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ['email', 'telefone', 'alternativo']


class EnderecoModelForm(forms.ModelForm):
    
    class Meta:
        model = Endereco
        fields = ['cidade', 'bairro', 'quarteirao', 'casa', 'avenida']
    


class EstudanteModelForm(forms.ModelForm):
    
    class Meta:
        model = Estudante
        fields = ['endereco', 'contacto', 'nome', 'dataNasc', 'doc_type', 'num_doc']