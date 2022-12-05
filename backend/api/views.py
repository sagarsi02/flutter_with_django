from .models import TODO
from .serializers import TODOSerializer
from rest_framework import generics

# Create your views here.
class TODOList(generics.ListCreateAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer

class TODOUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer