from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from catalog.models import Product


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"

# class HomePageView(TemplateView):
#     template_name = "base.html"



# class HomeView(TemplateView):
#     template_name = 'catalog/base.html'
# def home(request):
#     return render(request, 'base.html')
#
# #
# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, "product_detail.html", context)


# Задание 19.1
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) написал: {message}')
    return render(request, "contacts.html")

