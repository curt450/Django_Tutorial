from django.forms import modelForm
from .models import Room
from django.contrib.auth.models import User

class RoomForm(modelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(modelForm):
    class Meta:
        model = ['username, email']