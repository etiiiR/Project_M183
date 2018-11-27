from django.shortcuts import render
from .models import Bankaccoount

# Create your views here.
from django.views import generic

class BookListView(generic.ListView):
    model = Bankaccoount