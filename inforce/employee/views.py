from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Vote
from .serializers import VoteSerializer
from .permissions import IsEmployee

# Create your views here.


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.get_today_votes()
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated, IsEmployee)

    @action(detail=False, methods=["GET"])
    def result(self, request):
        vote_results = (
            self.queryset.values("menu")
            .annotate(count=Count("menu"))
            .order_by("-count")
        )
        winner = max(vote_results, key=lambda x: x["count"])
        response_data = {"winner": winner if winner else None, "results": vote_results}
        return Response(response_data)
