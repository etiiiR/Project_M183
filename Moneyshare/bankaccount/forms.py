from django import forms
from .models import Transaktion, Bankaccoount

class FolderForm(forms.ModelForm):
    class Meta:
       model = Transaktion
       fields = ['Money_from', 'Money_to', 'Value']
       user = ''

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(FolderForm, self).__init__(*args, **kwargs)
       self.fields['Money_from'].queryset = Bankaccoount.objects.filter(User=user)
       self.user = self.fields['Money_from'].queryset

    def sendtransaktion(self):
        pass