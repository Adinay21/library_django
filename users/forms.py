from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

CHOICES = (
        ('jun', 'jun'),
        ('middle', 'middle'),
        ('senior', 'senior')
    )

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    level = forms.ChoiceField(required=True, label='Your Level', choices=CHOICES)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'level'
        )

        def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.level = self.cleaned_data['level']

            if commit:
                user.save()
            return user