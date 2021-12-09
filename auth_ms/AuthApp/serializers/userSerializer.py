from rest_framework import serializers
from AuthApp.models.user import User
from AuthApp.models.rol import Rol

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password','name','last_name','cedula','create_time','email','rol']
 
    def to_representation (self, obj): #obj es usuario
        userData = User.objects.get(id=obj.id)
        rolData = Rol.objects.get(id=obj.rol_id) ##trae el campo rol en donde el id de rol sea igual al del objeto de usuario atributo rol_id
        return{
            'username':userData.username,
            'name':userData.name,
            'last_name':userData.last_name,
            'cedula':userData.cedula,
            'create_time':userData.create_time,
            'email':userData.email,
            'rol':{
               'name':rolData.name,
                'description':rolData.description,
            }
        }