from.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
class NewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']

class AddEmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
