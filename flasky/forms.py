from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['product', 'message']
        widgets = {
            'product': forms.HiddenInput(),
        }