from django.urls import path
from .views import TodosView, TodoView

urlpatterns = [
    path('', TodosView.as_view()),
    path('<int:pk>/', TodoView.as_view())
]