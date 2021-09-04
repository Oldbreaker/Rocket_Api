from rest_framework.generics import CreateAPIView,  RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAdminUser
from .serializers import UserSerializer
from .models import MyUser

# view para crear un usuario


class CreateUser(CreateAPIView):
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()
    permission_classes = [IsAdminUser]

# view para obtener un usuario por pk


class RetrieveUser(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()
    permission_classes = [IsAdminUser]

# view para borrar un usuario por pk


class DestroyUser(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()
    permission_classes = [IsAdminUser]

# view para modificar un usuario por pk


class UpdateUser(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = MyUser.objects.all()
    permission_classes = [IsAdminUser]
