from django import forms
from .models import Trip


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['traveler_name', 'traveler_email', 'start_date', 'end_date', 'guests', 'notes']
        widgets = {
            'traveler_name': forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'input'}),
            'traveler_email': forms.EmailInput(attrs={'placeholder': 'Your email', 'class': 'input'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
            'guests': forms.NumberInput(attrs={'min': 1, 'class': 'input'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Notes (optional)', 'class': 'input', 'rows': 3}),
        }
