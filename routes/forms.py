from django import forms
from .models import Airport


# Form to Add Airport Nodes

class AirportNodeForm(forms.Form):
    parent_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        required=False,
        empty_label="-- Root Airport --"
    )

    position = forms.ChoiceField(
        choices=[('left', 'Left'), ('right', 'Right')],
        required=False
    )

    airport_code = forms.CharField(max_length=10)
    duration = forms.IntegerField(min_value=1)


# Form to Search Nth Node in a Direction

class DirectionSearchForm(forms.Form):
    start_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        label="Select Airport"
    )
    direction = forms.ChoiceField(
        choices=[('left', 'Left'), ('right', 'Right')],
        label="Select Direction"
    )
