
from typing import AsyncGenerator
from django import forms


class HeartDataForm(forms.Form):

    SEX = [('M', 'Male'), ('F', 'Female')]
    EXER = [('Y', 'yes'), ('N', 'no')]
    CHEST_PAIN = [(0, 'typical angina'),
                  (1, 'atypical angina'),
                  (2, 'non-anginal pain'),
                  (3, 'asymptomatic')]
    FBS = [(1, 'yes'), (0, 'no')]
    ELECTRO = [(0, '0'), (1, '1'), (2, '2')]
    THAL = [(1, 'normal'), (2, 'reversible_defect'), (3, 'fixed_defect')]

    Age = forms.IntegerField(initial=30)
    Gender = forms.ChoiceField(choices=SEX)

    Chest_pain_type = forms.ChoiceField(choices=CHEST_PAIN)
    Resting_blood_pressure_trestbps = forms.IntegerField(initial=130)
    cholestrol = forms.IntegerField(initial=230)
    Fasting_blood_sugar_greater_than_120_mg__per_dl_fbs = forms.ChoiceField(
        choices=FBS)
    Resting_Electrocardiographic_Results_restecg = forms.ChoiceField(
        choices=ELECTRO)
    Maximum_heart_rate_thalatch = forms.IntegerField(initial=170)
    Exercise_exang = forms.ChoiceField(choices=EXER)
    Depression_level = forms.FloatField(initial=0.6)
    Slope_of_blood_cell = forms.IntegerField(initial=1)
    Number_of_vessels = forms.IntegerField(initial=2)
    results_of_thallium_stress_test = forms.ChoiceField(choices=THAL)
