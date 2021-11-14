from rest_framework                       import status, views
from rest_framework.response              import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from AuthApp.models.user                    import User
from AuthApp.serializers.userSerializer     import UserSerializer

class UserCreateView(views.APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data) #CRea el serializer, Recibe del json y lo convierte al objeto  que corresponda (request data es lo que llega en el body del postman)
        serializer.is_valid(raise_exception=True) # valida si los datos que recibe en el body (request.data) son los mismos que en el serializer
        serializer.save() #Guarda esos objetos en la base de datos/insert
        #Si el serializer confirma que el json recibido es correcto, crea el token de autenticacion

        tokenData = {"username":request.data["username"], 
                     "password":request.data["password"]}
        try:
            tokenSerializer = TokenObtainPairSerializer(data=tokenData) #CRea los tokens de refresh y access
            tokenSerializer.is_valid(raise_exception=True)
            return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("ERROR", e)
            return Response('Error in token generation', status=status.HTTP_500_INTERNAL_SERVER_ERROR)