from django import forms
from .models import Question

class CreateQuestionForm(forms.ModelForm):
    type = forms.CharField(widget=forms.TextInput(attrs={'class': 'text-input'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text-input'}))
    frequency = forms.CharField(widget=forms.TextInput(attrs={'class': 'text-input'}))

    class Meta:
        model = Question
        fields = [
            'type',
            'text',
            'frequency'
        ]