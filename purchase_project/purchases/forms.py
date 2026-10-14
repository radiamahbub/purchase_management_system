from django import forms
from purchases.models import *

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = '__all__'
        exclude = ['user']

class SupplierForm(forms.ModelForm):
    class Meta:
        models = SupplierModel
        fields = '__all__'
        exclude = ['user']
