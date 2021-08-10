from django.forms import ModelForm
from .models import Feedback
from django import forms


# Create the form class.
class FeedbackForm(ModelForm):
    required_css_class = "field"

    class Meta:
        model = Feedback
        fields = ['name', 'phone_number', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'phone_number': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'text': forms.Textarea(attrs={'class': 'input_message'}),
        }
