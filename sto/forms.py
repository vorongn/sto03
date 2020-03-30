from . import models
from django import forms
from django.forms import ModelForm


class ClientForm(ModelForm):

    class Meta:
        model = models.Client
        fields = ('first_name', 'last_name', 'phone_number',
                  'photo', 'status', 'description', 'cars')


class CarForm(ModelForm):

    class Meta:
        model = models.Car
        fields = ('vin', 'brend_car', 'model_car', 'year',
                  'motor', 'transmission', 'number',
                  'photo', 'description')


class RepairForm(ModelForm):

    class Meta:
        model = models.Repair
        fields = ('car', 'car_mileage', 'date', 'repworks',
                  'description', 'repair_cost', 'photo01',
                  'photo02', 'photo03')


class WorksForm(forms.Form):
    work = forms.CharField()
    description = forms.Textarea
