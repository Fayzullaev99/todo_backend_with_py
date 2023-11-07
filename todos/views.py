from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Todos
from .serializers import TodosSerializer


# Create your views here.

class TodosView(ListAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer


class TodoView(RetrieveAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer


from django.shortcuts import render

# Create your views here.
