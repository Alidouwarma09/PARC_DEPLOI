from django import forms
from django.forms import ClearableFileInput
from django.forms.widgets import Input

from Model.models import Vehicule, Marque


class XYZ_DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs.setdefault('attrs', {})
        kwargs['attrs'].update({
            'class': 'form-control',
            'required': False,
        })
        kwargs["format"] = "%m-%d-%Y"
        # kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)


class XYZ_DateInpute(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs.setdefault('attrs', {})
        kwargs['attrs'].update({
            'class': 'form-control',
            'required': False,
        })
        kwargs["format"] = "%m-%d-%Y"
        # kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)


class MultipleFileInput(Input):
    template_name = 'ajouter_vehicule.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['value'] = value
        return context


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = '__all__'

    marque = forms.ModelChoiceField(queryset=Marque.objects.all(), required=True)
    image = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}), required=False)

    def __init__(self, *args, **kwargs):
        super(VehiculeForm, self).__init__(*args, **kwargs)
        self.fields['marque'].widget.attrs.update({
            'class': "form-control",
            'id': "selectMarque",
            'required': True,
        })
        self.fields['kilometrage'].required = True
        self.fields['date_d_edition'].required = True
        self.fields['image'].required = True
        self.fields['carte_grise'].required = True
        self.fields['date_expiration_assurance'].required = True
        self.fields['date_videnge'].required = True
        self.fields['type_commercial'].required = True


class VehiculSearchForm(forms.Form):
    q = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Rechercher un vehicul: Marque, model, matricule...', 'class': 'form-control'}),
    )


class marqueForm(forms.ModelForm):
    class Meta:
        model = Marque
        fields = '__all__'
