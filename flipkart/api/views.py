from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product
from django.views.generic import CreateView
import re

def isValidURl(url):
    regex = "^((http|https)://)?([-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*))$"
    if re.match(regex, url):
        return True
    else:
        return False

from .utils import scrapData
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SearchViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_queryset(self):
        self.queryset = Product.objects.filter( link__icontains=self.request.GET.get('q') )
        # No data found in database
        if( self.queryset.count() == 0 ):
          data = scrapData(self.request.GET.get('q'))
          print(data)
        return self.queryset

#  Home page view
class Home(CreateView ):
    template_name = 'home.html'
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'home.html', {'products': products})