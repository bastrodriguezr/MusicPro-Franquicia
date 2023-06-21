from django import forms
from .models import Producto,Transporte,DireccionEnvio
from .validators import MaxSizeFileValidator
 

class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=3)])
    precio = forms.IntegerField(min_value=1, max_value=1500000)


    class Meta:
        model = Producto
        fields = '__all__'

        #en caso de necesitar ingresar una fecha, se debe agregar el siguiente campo:
        #   widgets = {
        #       'fecha-fabricacion': forms.SelectDateWidget()
        #   }
        #fin de la fecha

class TransporteForm(forms.ModelForm):

    class Meta:
        model = Transporte
        fields = ["direccion_envio"]

class DireccionEnvioForm(forms.ModelForm):
    direccion = forms.CharField(max_length=100)

    class Meta:
        model = DireccionEnvio
        fields = ["direccion"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        direccion_guardada = kwargs.get('instance')
        if direccion_guardada:
            self.initial['direccion'] = direccion_guardada.direccion
