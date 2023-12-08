"""Forms of the project."""

# Create your forms here.
# things/forms.py
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        exclude = ['created_at']  # Exclude the 'created_at' field from the form
        widgets = {
            'description': forms.Textarea(),  # Display 'description' as a Textarea
            'quantity': forms.NumberInput(),  # Display 'quantity' as NumberInput
        }
