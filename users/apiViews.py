from rest_framework.viewsets  import ModelViewSet
from rest_framework.permissions import AllowAny

from .serializers import SignUpUserSerializer
from .models import User

class SignUpView(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = SignUpUserSerializer
    http_method_names = ['post']