from rest_framework import viewsets
from app.serializers import UserSerializer
from .models import User
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-pk')
    serializer_class = UserSerializer
