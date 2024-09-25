from django.forms import modelForm
from .models import Room


class RoomForm(modelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']