from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ContactView(TemplateView):
    template_name = 'contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо, {name}! Сообщение получено!')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'
