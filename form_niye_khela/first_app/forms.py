from django import forms 

class contactform(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    
    def clean(self):
        cleaned_data = super().clean()

        valname = cleaned_data['name']
        valemail = cleaned_data['email']

        if len(valname) <10 :
            raise forms.ValidationError('Bro naam arektu boro theke thik koro')
        if '.com' not in valemail :
            raise forms.ValidationError('.com hode bhaia ?')
        
   
