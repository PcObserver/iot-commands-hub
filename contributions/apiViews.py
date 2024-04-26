from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Contribution, ContributionReview
from .serializers import ContributionPolymorphicSerializer, ContributionReviewSerializer


class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionPolymorphicSerializer
    http_method_names = ["get", "post"]

    @action(detail=True, methods=["get"], serializer_class=ContributionReviewSerializer)
    def reviews(self, request, pk=None):
        contribution = self.get_object()
        contribution_reviews = contribution.reviews.all()
        serializer = self.get_serializer(contribution_reviews, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ContributionReviewViewSet(viewsets.ModelViewSet):
    queryset = ContributionReview.objects.all()
    serializer_class = ContributionReviewSerializer
    http_method_names = ["get", "post"]
