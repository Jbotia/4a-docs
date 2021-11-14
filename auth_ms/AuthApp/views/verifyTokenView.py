from django.conf                            import settings #confg del proyecto (AuthModule.settings) para sacar algoritmo de codigicacion
from rest_framework                         import status   #cod respuesta html
from rest_framework.response                import Response #Respuesta personalizada de cod html
from rest_framework_simplejwt.views         import TokenVerifyView #Vista para verificar el token
from rest_framework_simplejwt.backends      import TokenBackend #donde se coloca el algoritmo para decodificar Tokens
from rest_framework_simplejwt.exceptions    import InvalidToken, TokenError 
from rest_framework_simplejwt.serializers   import TokenVerifySerializer #Serializer que retorna json con respuesta, dependendo del resultado de verificar el token

class VerifyTokenView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        serializer = TokenVerifySerializer(data=request.data) #CRea el serializer, Recibe del json y lo convierte al objeto  que corresponda
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM']) #Genera algoritmo para decodificar token
        try:
            serializer.is_valid(raise_exception=True)
            token_data = tokenBackend.decode(request.data['token'],verify=False) #Decodifica el token que recibe (del body en request.data)
            serializer.validated_data['UserId'] = token_data['user_id']
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)