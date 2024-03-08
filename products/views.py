from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'index.html')

def products(request):
    all_products = Product.objects.all().order_by('created_at')
    paginator = Paginator(all_products, 8)
    
    page = request.GET.get('page')
    products = paginator.get_page(page)

    page_num = products.number
    page_set_1 = products.paginator.page_range[:4]
    page_set_2 = products.paginator.page_range[page_num-2:page_num+1]
    
    return render(request, 'products.html', {'products': products,
                                             'page_set_1': page_set_1,
                                             'page_set_2': page_set_2})

def product_details(request):
    return render(request, 'product_details.html')
