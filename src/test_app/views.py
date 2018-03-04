from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from . models import Product


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', )

    def get_success_url(self):
        return reverse('test_app:product-detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('test_app:product-list')


class ProductDetailView(DetailView):
    model = Product


class ProductListView(ListView):
    model = Product
