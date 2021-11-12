from rest_framework import serializers 
from AuthApp.models.user import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password','rol', 'name', 'email']