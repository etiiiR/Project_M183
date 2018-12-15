from django import forms
from .models import Transaktion, Bankaccoount

class sendmoneytofriend(forms.Form):
    send_money_value = forms.IntegerField()
    send_money_to = forms.CharField()
    
    message = forms.CharField(widget=forms.Textarea)

    def sendmoney(self):
        # send email using the self.cleaned_data dictionary
        pass


class FolderForm(forms.ModelForm):
    class Meta:
       model = Transaktion
       fields = ['Money_from', 'Money_to', 'Value']

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(FolderForm, self).__init__(*args, **kwargs)
       self.fields['Money_from'].queryset = Bankaccoount.objects.filter(User=user)
