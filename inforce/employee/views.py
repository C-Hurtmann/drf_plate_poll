from rest_framework import viewsets

from .models import Vote
from .serializers import VoteSerializer

# Create your views here.
class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer