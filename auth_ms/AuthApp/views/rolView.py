from django.conf                          import settings
from rest_framework                       import status, views,generics
from rest_framework.response              import Response
from rest_framework_simplejwt.backends    import TokenBackend
from rest_framework.permissions           import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from AuthApp.models.rol                import Rol
from AuthApp.serializers.rolSerializer import RolSerializer

class RolDetailView(generics.RetrieveAPIView):
    queryset = Rol.objects.all() #valida cuales roles puede buscar y los guarda en ram
    serializer_class = RolSerializer
    def get(self, request, *args, **kwargs):  #Se indica de forma explicita la forma de extrart datos (el metodo es opcional)
        return super().get(request, *args, **kwargs)

class RolCreateView(generics.CreateAPIView):
    serializer_class = RolSerializer
    #crea rol, es otra forma de hacerlo en comparación con la de user donde se maneja la excepcion dentro del metodo is valid
    def post(self, request,*args,**kwargs):
        serializer = RolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)           