from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserRegistrationSerializer, CustomTokenPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = CustomUser.objects.none()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serialized_data = self.get_serializer(data=request.data)
        if serialized_data.is_valid():
            self.perform_create(serialized_data)
            return Response({'message': 'User registered successfully.', 'data': serialized_data.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenPairSerializer
