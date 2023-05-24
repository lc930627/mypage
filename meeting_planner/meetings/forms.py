from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from .models import Meeting


class MeetingForm(forms.ModelForm):
    participants = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    def clean_date(self):
        d = self.cleaned_data.get("date")
        if d < date.today():
            raise ValidationError("Mypage cannot be in the past")
        return d

    def clean_participants(self):
        participants = self.cleaned_data.get('participants')

        email_list = [email.strip() for email in participants.split(',') if email.strip()]

        if len(email_list) != len(set(email_list)):
            raise ValidationError("Duplicate email addresses are not allowed.")

        for email in email_list:
            if '@' not in email:
                raise ValidationError("Invalid email address: {}".format(email))

        return participants

    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={"type": "date"}),
            'start_time': forms.TimeInput(attrs={"type": "time"}),
            'duration': forms.TextInput(attrs={"type": "number", "min": "1", "max": "4"}),
            'participants': forms.Textarea(attrs={'rows': 3}),
            'notes': forms.TextInput(attrs={"type": "text"})
        }
