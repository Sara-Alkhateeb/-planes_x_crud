from django.urls import path
from .views import PlaneListView, PlaneDetailView, PlaneCreateView, PlaneUpdateView, PlaneDeleteView

urlpatterns = [
    path('planes/', PlaneListView.as_view(), name='plane_list'),
    path('<int:pk>/', PlaneDetailView.as_view(), name='plane_detail'),
    path('create/', PlaneCreateView.as_view(), name='plane_create'),
    path('<int:pk>/update/', PlaneUpdateView.as_view(), name='plane_update'),
    path('<int:pk>/delete/', PlaneDeleteView.as_view(), name='plane_delete'),
]