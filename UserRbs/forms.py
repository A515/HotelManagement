from django import forms
from UserRbs.models import RoleDetails


class RoleDetailsForm(forms.ModelForm):
    class Meta:
        model = RoleDetails
        exclude = ["role"
                   "name"
                   "email"
                   "password"
                   "mobile"
                   "address"
                   "gender"
                   "image"
                   "otp"
                   "otp_time"
                   "verify_link"
                   "login_time"
                   "active"]
