from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import UserCreateSerializer
# Create your views here.

class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer