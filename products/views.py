from django.shortcuts import render
from django.views.generic import ListView, DetailView 

from .models import Product

# Create your views here.
class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = 'products/product_list.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		return context

class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = 'products/product_detail.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		return context
