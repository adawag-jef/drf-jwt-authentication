from rest_framework.generics import ListAPIView
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserList(ListAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()