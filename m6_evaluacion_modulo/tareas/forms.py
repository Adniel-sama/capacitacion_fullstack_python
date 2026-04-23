from django import forms 

class TareaForm(forms.Form):
    nombre = forms.CharField(max_length=60, label="Nombre")
    estado = forms.CharField(max_length=60, label="Estado")
    descripcion = forms.CharField(widget=forms.Textarea,label="Descripción")

  