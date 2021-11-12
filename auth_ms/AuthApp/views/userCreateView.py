#from django.forms.models import _Fields
from rest_framework import status, views, generics
from rest_framework.response import Response
from django.views import generic
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from AuthApp.models import User
from AuthApp.serializers import UserSerializer

from AuthApp.serializers.userSerializer import UserSerializer

class UserCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    '''def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"username":request.data["username"], 
                     "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
                
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)'''