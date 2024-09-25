from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from main.models import MoodEntry

class MoodEntryForm(ModelForm):
    class Meta:
        model = MoodEntry
        fields = ["mood", "feelings", "mood_intensity"]
        widgets = {
            'mood': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your mood'}),
            'feelings': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your feelings'}),
            'mood_intensity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rate intensity from 1 to 10'}),
        }

class RegisterUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(RegisterUser, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs.update({'class': 'form-control', 'style': 'width: 30rem;'})