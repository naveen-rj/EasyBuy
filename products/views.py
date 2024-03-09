from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    
    featured_products = Product.objects.order_by('-priority')[:4]
    latest_products = Product.objects.order_by('-created_at')[:8]
    
    return render(request, 'index.html', {'featured_products': featured_products,
                                          'latest_products': latest_products})

def products(request):
    
    all_products = Product.objects.order_by('created_at')
    paginator = Paginator(all_products, 8)
    
    page = request.GET.get('page')
    products = paginator.get_page(page)

    page_num = products.number
    page_set_1 = products.paginator.page_range[:4]
    page_set_2 = products.paginator.page_range[page_num-2:page_num+1]
    
    return render(request, 'products.html', {'products': products,
                                             'page_set_1': page_set_1,
                                             'page_set_2': page_set_2})

def product_details(request, pk):
    
    product = Product.objects.get(pk=pk)
    related_products = Product.objects.exclude(pk=pk)[:4]
    
    return render(request, 'product_details.html', {'product': product, 'related_products': related_products})
