from django.contrib.auth.forms import UserCreationForm

from petsapp.models import Login

##doctor requirements
class doctor_form(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2','name','age','contact_no','address','qualification')

##
class user_form(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2','name','age','contact_no','address')
