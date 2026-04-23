from django import forms
from .models import Producto, Categoria, Etiqueta, DetalleProducto

class ProductoForm(forms.ModelForm):
    dimensiones = forms.CharField(required=False, max_length=120)
    peso_kg = forms.DecimalField(required=False, max_digits=8, decimal_places=3)
    info_adicional = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'etiquetas']
        widgets = {
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'step': 1,
                'placeholder': '$'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and getattr(self.instance, 'detalle', None):
            det = self.instance.detalle
            self.fields['dimensiones'].initial = det.dimensiones
            self.fields['peso_kg'].initial = det.peso_kg
            self.fields['info_adicional'].initial = det.info_adicional

    def save(self, commit=True):
        producto = super().save(commit=False)
        if commit:
            producto.save()
            dimensiones = self.cleaned_data.get('dimensiones') or ''
            peso_kg = self.cleaned_data.get('peso_kg')
            info_adicional = self.cleaned_data.get('info_adicional') or ''

            hay_detalle = bool(dimensiones.strip() or peso_kg is not None or info_adicional.strip())

            if hay_detalle:
                if getattr(producto, 'detalle', None):
                    det = producto.detalle
                    det.dimensiones = dimensiones
                    det.peso_kg = peso_kg
                    det.info_adicional = info_adicional
                    det.save()
                else:
                    det = DetalleProducto.objects.create(
                        dimensiones=dimensiones,
                        peso_kg=peso_kg,
                        info_adicional=info_adicional
                    )
                    producto.detalle = det
                    producto.save()
            else:

                pass

            if 'etiquetas' in self.cleaned_data:
                self.save_m2m()

        return producto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']


class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']
