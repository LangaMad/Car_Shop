from django.shortcuts import render
from .models import Car
from django.views.generic import  ListView,DetailView
from django_filters.views import FilterView
from .filters import CarFilter
from django.db.models import Q
# Create your views here.

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
    template_name = 'index.html'
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

print('Heloo')
print('Hello TIlek' "SOLID SOLID")

print("Daniyar")

print('baku')

print("ПРИВЕТ от Айдара")

print('че шаурму похаваем ?')
print('че Похавали шаурму ?')