from django import forms

class Formulario(forms.Form):
    nome = forms.CharField(max_length=40)
    sobrenome = forms.CharField(max_length=50)
    cpf = forms.CharField(max_length=14,min_length=11)
    tempo_de_servico = forms.IntegerField()
    remuneracao = forms.DecimalField(max_digits=8)