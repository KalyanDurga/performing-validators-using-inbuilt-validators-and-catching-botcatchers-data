from django import forms

def check_for_a(name):
    if name[0].lower()=='a':

        raise forms.ValidationError('name stared with a')


class Studentform(forms.Form):
    name=forms.CharField(max_length=50,validators=[check_for_a])
    age=forms.IntegerField()
    email=forms.EmailField()
    Re_Enter_Email=forms.EmailField()
    bot=forms.CharField(max_length=50,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data.get('email')
        r=self.cleaned_data['Re_Enter_Email']
        if e!=r:
            raise forms.ValidationError('email not matched')

    def clean_bot(self):
        b=self.cleaned_data.get('bot')
        if len(b)>0:
            raise forms.ValidationError('botcatcher dat insertion')
