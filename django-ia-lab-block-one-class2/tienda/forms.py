from django import forms
from django.forms import inlineformset_factory
from .models import Producto,Cliente,Pedido, PedidoItem

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Nombre del producto"
            }),
            "descripcion": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Breve descripción"
            }),
            "precio": forms.NumberInput(attrs={
                "step": "0.01",
                "min": 0
            }) 
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo']  

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Nombre completo",
                "class": "form-control"
            }),
            "correo": forms.EmailInput(attrs={
                "placeholder": "Correo electrónico",
                "class": "form-control"
            }),
        }

class PedidoSimpleForm (forms.ModelForm)
    class Meta:
        model= Pedido
        fields= ['cliente', 'estado']

class PedidoItemForm (forms.ModelForm)
    class Meta:
        model= PedidoItem
        fields= ['producto', 'cantidad','precio_unitario']
        widgets={
            "cantidad":forms.NumberInput(attrs={
                "min":1,
                "step":"1"
            }),
            "precio_unitario": forms.NumberInput(attrs={
                "step": "0.01"
                "min":0
            })
        }

PedidoItemFormSet = inlineformset_factory(
    parent_model=pedido,
    model=PedidoItem,
    form=PedidoItemForm,
    extra= 1,
    can_delete=True,
)