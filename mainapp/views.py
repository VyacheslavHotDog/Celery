from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView
from mainapp.forms import ProductForm
from mainapp.models import Product
from rest_framework import viewsets
from rest_framework.response import Response
from mainapp.serializers import ProductSerializer

class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'product_list'
    queryset = Product.objects.all().order_by('name')


class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'add_product.html'


class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    template_name = 'your_template.html'

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(user)
        return Response(serializer.data)
