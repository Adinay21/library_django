from django import forms
from . import models, parser_top

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('top', 'top'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            "media_type"
        ]
    def parser_data(self):
        if self.data['media_type'] == 'top':
            top_file = parser_top.parsing()
            for i in top_file:
                models.TopModel.objects.create(**i)

