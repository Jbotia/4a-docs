from rest_framework import serializers
from AuthApp.models.rol import Rol
#recibe objeto y convierte a json y viceversa

class RolSerializer(serializers.ModelSerializer): 
    class Meta: #Meta,es la metadada que va a a tener la clase / 
        model = Rol
        fields = ['name','description']
        
    def to_representation(self,obj):
        rol = Rol.objects.get(id = obj.id) #De el dao que usa "objects" trae los roles donde el id del obj actual(self) se igual al de la tabla
        return{
            'name': rol.name,
            'description': rol.description
        }