from django import forms
from .models import Road


class RoadForm(forms.ModelForm):
    class Meta:
        model = Road
        fields = "__all__"

        widgets = {
            "contractor_name": forms.TextInput(attrs={'class': 'class-controls'}),
            "KM_price": forms.NumberInput(attrs={'class': 'class-controls'}),
            "road_no": forms.NumberInput(attrs={'class': 'class-controls'}),
            "maintaince_price": forms.NumberInput(attrs={'class': 'class-controls'}),
            "payment_mode": forms.Select(attrs={'class': 'class-controls'}),
            "road_length": forms.Select(attrs={'class': 'class-controls'}),
        }
