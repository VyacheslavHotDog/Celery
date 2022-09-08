from django.shortcuts import get_object_or_404
from mainapp.models import Product
from rest_framework import viewsets
from rest_framework.response import Response
from mainapp.serializers import ProductSerializer
from pdf_django.tasks import sample_task
from rest_framework.decorators import action


class ProductViewSet(viewsets.ViewSet):
    """
    A simple ViewSet
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request):
        queryset = Product.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(product)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        pdf_data = {
            'name': instance.name,
            'countBefore': instance.count,
            'countAfter': request.data['count'],
        }
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        sample_task.delay(pdf_data)

        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def increase_count(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        instance.increase_count()
        return Response(instance.count)

    @action(detail=True, methods=['post'])
    def decrease_count(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        instance.decrease_count()
        return Response(instance.count)
