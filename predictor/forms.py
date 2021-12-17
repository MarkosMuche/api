
from typing import AsyncGenerator
from django import forms


class HeartDataForm(forms.Form):

    SEX = [('M', 'Male'), ('F', 'Female')]
    EXER = [('Y', 'yes'), ('N', 'no')]

    Age = forms.IntegerField()
    Gender = forms.ChoiceField(choices=SEX)

    CP = forms.IntegerField()
    Resting_blood_pressure_trestbps = forms.IntegerField()
    cholestrol = forms.IntegerField()
    Fasting_blood_sugar_fbs = forms.IntegerField()
    Resting_Electrocardiographic_Results_restecg = forms.IntegerField()
    Maximum_heart_rate_thalatch = forms.IntegerField()
    Exercise_exang = forms.ChoiceField(choices=EXER)
    Depression_level = forms.IntegerField()
    Slope_of_blood_cell = forms.IntegerField()
    Number_of_vessels = forms.IntegerField()
    maximum_heart_rate_achieved = forms.IntegerField()
