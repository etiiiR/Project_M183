from django import forms

class sendmoneytofriend(forms.Form):
    send_money_value = forms.IntegerField()
    send_money_to = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def sendmoney(self):
        # send email using the self.cleaned_data dictionary
        pass