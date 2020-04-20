from django import forms

from .models import Whisky, Metal


class WhiskyForm(forms.ModelForm):
    class Meta:
        model = Whisky
        fields = ('img', 'name', 'price', 'strength', 'size', 'type', 'distillery', 'bottler', 'casktype', 'casknumber',
                  'vintage', 'serie', 'bottled', 'bottled', 'age', 'bottles_in_serie')

class MetalForm(forms.ModelForm):
    class Meta:
        model = Metal
        fields = ('img', 'name', 'price', 'type', 'alloy', 'weight', 'diameter', 'denomination', 'mintage_pcs', 'edge',
                  'quality', 'producer')
