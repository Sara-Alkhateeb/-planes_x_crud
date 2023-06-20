from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Plane


class PlaneListView(ListView):
    template_name = "planes/planeList.html"
    model = Plane


class PlaneDetailView(DetailView):
    template_name = "planes/planeDetail.html"
    model = Plane


class PlaneCreateView(CreateView):
    template_name = "planes/planeCreat.html"
    model = Plane
    fields = ['name','Manufacturer', 'Cost', 'Year_Published', 'Reviewer']


class PlaneUpdateView(UpdateView):
    template_name = "planes/planeUpdate.html"
    model = Plane
    fields = '__all__'
    success_url = reverse_lazy("plane_list")


class PlaneDeleteView(DeleteView):
    template_name = "planes/planeDelete.html"
    model = Plane
    success_url = reverse_lazy("plane_list")
