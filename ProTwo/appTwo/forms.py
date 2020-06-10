from django import forms
from django.contrib.auth.models import User
from appTwo.models import ClientInfo,Booking

class ClientDefaultInfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientDefaultInfoForm,self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                     'class': 'form-control'
                 })
    class Meta():
        date = forms.DateField(input_formats=['%Y-%m-%d','%m/%d/%Y','%d/%m/%y'])
        model = User
        fields = ('username', 'email', 'password')
        labels = {
                "username":'Username :',
                "email":'Email Addr:',
                "password":'Password :',
        }
        widgets = {
        'username': forms.TextInput(attrs={'placeholder':'example: Touray'}),
        'email': forms.TextInput(attrs={'placeholder':'example: touray@gmail.com'}),
        'password': forms.PasswordInput(attrs={'placeholder':''})

        }
#THIS IS THE FORM FOR THE EXTENDED FIELDS
class ClientInfoForm(forms.ModelForm):
    #THIS CODE FORMATS THE FORM FIELD IN A NICE WAY
    def __init__(self, *args, **kwargs):
        super(ClientInfoForm,self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                     'class': 'form-control'
                 })
    class Meta():
        model = ClientInfo #never put a capital letter on 'models'
        fields = ('date','phone_number')
        labels = {
                "date":'Select Date:',
                "phone_number":'Phone No.  :'
            }
        widgets = {
        'date': forms.TextInput(attrs={'placeholder':'example: 2020-05-30'}),
        'phone_number': forms.TextInput(attrs={'placeholder':'example: 9999999'})
        } #ADDING STUFFS LIKE placeholder TO THE FORM FOR GUIDE

#DEFINING THE FORM FOR THE APPOINTMENT MODEL(where users can book appointment)
class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookingForm,self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                 'class': 'form-control'
             })
    class Meta():
        model = Booking
        fields = ('username','email','date','phone_number')
        labels = {
            "username":'Username:',
            "email":'Email Address:',
            "date":'Select Date:',
            "phone_number":'Phone No:'
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder':'example: Omar'}),
            'email': forms.TextInput(attrs={'placeholder':'example: omartouray@gmail.com'}),
            'date': forms.TextInput(attrs={'placeholder':'example: 2020-05-30'}),
            'phone_number': forms.TextInput(attrs={'placeholder':'example: 9999999'})
        }
