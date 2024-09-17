from django.forms import ModelForm
from django import forms
from touristapp2.models import *

class DateInput(forms.DateInput):
   input_type='date'

class Membershipform(ModelForm):
    class Meta:
        model=Membershipmodel
        fields=['name','email','phone_number','country','special_request']
    def clean(self):
        super().clean()
        return self.cleaned_data
        
class Bookingform(ModelForm):
    class Meta:
        model=Bookingmodel
        fields=['name','email','check_in_date','check_out_date',
                'destination','no_of_persons','have_you_availed_membership',
                'type_of_room'
                ]
        widgets={'check_in_date':DateInput,'check_out_date':DateInput}#when widgets are mentioned, django uses it to
    def clean(self):                                            #change the html for that field. render means 'convert to html'
        super().clean()
        return self.cleaned_data
    

class Feedbackform(ModelForm):
    class Meta:
        model=Feedbackmodel
        fields=['name','feedback','home']
    def clean(self):
        super().clean()
        return self.cleaned_data
        
