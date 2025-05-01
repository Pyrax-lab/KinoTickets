from django import forms 
from kino.models import Locals


class FormBuyLocal(forms.Form):

    place = forms.IntegerField(required=True, label="Place", initial=0)


