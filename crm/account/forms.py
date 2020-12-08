from django import forms

class CustomerRegistration(forms.Form):
    firstname    = forms.CharField(min_length = 2, max_length = 50)
    lastname     = forms.CharField(min_length = 5, max_length = 50)
    email        = forms.EmailField()
    password     = forms.CharField(widget = forms.PasswordInput)
    rpassword    = forms.CharField(label = 'Confirm Password' , widget = forms.PasswordInput)
    

    def clean(self):
        cleaned_data = super().clean()
        fpass = self.cleaned_data['password']
        spass = self.cleaned_data['rpassword']

        if fpass != spass:
            raise forms.ValidationError('password not matched')
