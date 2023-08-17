from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Vote
from .serializers import VoteSerializer

# Create your views here.
class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)