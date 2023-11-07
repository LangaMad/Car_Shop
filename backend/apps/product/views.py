from django.shortcuts import render
from rest_framework.response import Response
from .models import Car,CarImage
from django.views.generic import  ListView,DetailView
from django_filters.views import FilterView
from .filters import CarFilter
from django.db.models import Q
from rest_framework.generics import *
from .serializers import CarSerializer,CarImageSerializer
from rest_framework.viewsets import *
from rest_framework.decorators import action
from rest_framework.permissions import *
from .permission import IsAdminOrReadOnly,IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination




class CarDeleteAPIview(DestroyAPIView):
    serializer_class =  CarSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)



class CarDetailAPIview(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated,)

class CarAPIListPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 3

class CarListAPIview(ListCreateAPIView):
    serializer_class = CarSerializer
    model = Car
    queryset = Car.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = CarAPIListPagination


























#
# class CarAllAPIview(ModelViewSet):
#     serializer_class = CarImageSerializer
#     queryset = CarImage.objects.all()
#
#     @action(methods=['get'],detail=False)
#     def car3(self,request):
#         car2 = CarImage.objects.all()
#         return Response({'car':[c.car.name for c in car2]})
#
#

#
# class CarCreateAPIview(CreateAPIView):
#     serializer_class = CarSerializer
#     queryset = Car.objects.all()
#
# class CarImageAPIview(ListAPIView):
#     serializer_class = CarImageSerializer
#     model = CarImage
#     queryset = CarImage.objects.all()
#
#
# class CarUpdateAPIview(UpdateAPIView):
#     serializer_class = CarSerializer
#     queryset = Car.objects.all()
#

#
# class CarImageCreateAPIview(CreateAPIView):
#     serializer_class = CarImageSerializer
#     queryset = Car.objects.all()
#

class ProductView(FilterView):
    model = Car
    template_name = 'index.html'
    filterset_class = CarFilter
    context_object_name = 'car'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CarFilter(self.request.GET, queryset=self.get_queryset())
        return context


class SearchCarView(ListView):
    template_name = 'search.html'
    model = Car

    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return self.model.objects.all()
        q = self.model.objects.filter(
            Q(name__icontains=search_text)
            |Q(description__icontains = search_text)

        )
        return q

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = True
        context['search_query'] = self.request.GET.get('query')

        return context

class DetailCarView(DetailView):
    template_name = 'car_detail.html'


































