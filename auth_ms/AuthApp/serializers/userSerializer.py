from rest_framework import serializers
from AuthApp.models.user import User
from AuthApp.models.rol import Rol

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password','name','last_name','cedula','create_time','email','rol']
 
    def to_representation (self, obj):
        user = User.objects.get(id = obj.id)
        rol = Rol.objects.get(id = user.id) ##trae el rol asociada al usuario, en donde el id del rol sea igual al campo user.id
        return{
            'username':user.username,
            'name':user.name,
            'last_name':user.last_name,
            'cedula':user.cedula,
            'create_time':user.create_time,
            'email':user.email,
            'rol':{
               'name':rol.name,
                'description':rol.description,
            }
        }