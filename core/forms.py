from django import forms
from .models import Member, MembershipPayment, Event, Expenditure

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone']

class MembershipPaymentForm(forms.ModelForm):
    class Meta:
        model = MembershipPayment
        fields = ['member', 'amount']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'event_date', 'income']

class ExpenditureForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ['description', 'amount']
