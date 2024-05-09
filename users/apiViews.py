from rest_framework.viewsets  import ModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import SignUpUserSerializer, UserSerializer
from .models import User
from .filters import UserFilter

class SignUpViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = SignUpUserSerializer
    http_method_names = ['post']

    
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter
    http_method_names = ['get', 'patch']