from rest_framework                         import status,generics
from django.conf                            import settings 

from AuthApp.models.user                    import User
from AuthApp.serializers.userSerializer     import UserSerializer

#Obtener informacion de un usuario
class UserDetailView(generics.RetrieveAPIView):
    queryset            = User.objects.all() #trae a traves del dao (objecto) todos los usuarios y los guarda en ram
    serializer_class    = UserSerializer
    def get(self, request, *args, **kwargs): #Se indica de forma explicita la forma de extrart datos (el metodo es opcional)
        return super().get(request, *args, **kwargs)

#actualizar un usuario
class UserUpdateView(generics.UpdateAPIView):
    queryset            = User.objects.all() #trae a traves del dao (objecto) todos los usuarios y los guarda en ram
    serializer_class    = UserSerializer
    def update(self, request, *args, **kwargs):           
        return super().update(request, *args, **kwargs)

#Eliminar un User, no recomendado
class UserDeleteView(generics.DestroyAPIView):
    queryset            = User.objects.all() #trae a traves del dao (objecto) todos los usuarios y los guarda en ram
    serializer_class    = UserSerializer
    def delete(self, request, *args, **kwargs):    
        return super().destroy(request, *args, **kwargs)