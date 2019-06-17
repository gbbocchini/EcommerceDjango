from .models import ContatoForm
from django import forms


class Form(forms.ModelForm):
    class Meta:
        model = ContatoForm
        fields = '__all__'

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'mensagem': forms.Textarea(attrs={'class': 'form-control'}),
    }