from django import forms


class contactUs(forms.Form):
    name = forms.CharField(label='Your Name', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'name'}), required=True)
    email = forms.EmailField(label='Email ID', error_messages={
                             'invalid': 'This is my email error msg.'}, widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailID'}), required=True)
    contactno = forms.IntegerField(label='Contact Number', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'id': 'contactno'}), required=False)
    subject = forms.CharField(label='Subject', max_length=75, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'subject'}), required=True)
    message = forms.CharField(label='Your Message', max_length=250, widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'message', 'rows': 4, 'cols': 15}), required=True)
