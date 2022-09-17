from django import forms
from.models import *

class StudentForm(forms.Form):
    ism=forms.CharField()
    st_raqam=forms.CharField(label=("student raqami"))
    guruh=forms.CharField()
    bitiruvchi=forms.BooleanField()
    kitob_soni = forms.IntegerField(max_value=5, min_value=0,)

class MuallifForm(forms.Form):
    ism=forms.CharField()
    jins=forms.ChoiceField(choices= [("Man","Man"), ("Woman", "Woman")])
    tirik=forms.BooleanField()
    tugulgan_yil=forms.DateField()
    kitob_soni = forms.IntegerField()

class RecordForm(forms.ModelForm):
    class Meta:
        model=Record
        fields='__all__'

class KitobForm(forms.ModelForm):
    class Meta:
        model=Kitob
        fields='__all__'