from rest_framework import viewsets
from .models import Contribution
from .serializers import ContributionPolymorphicSerializer

class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionPolymorphicSerializer
    http_method_names = ["get","post"]