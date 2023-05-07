from django.db.models import fields
from django.forms import ModelForm, TextInput
from .models import Channel

class ChannelForm(ModelForm):
    class Meta:
        model = Channel
        fields = ['keyword']
        widgets = {
            'keyword': TextInput(attrs={'class' : 'input', 'placeholder' : 'Keyword'}),
        } 