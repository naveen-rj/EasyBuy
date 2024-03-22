from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Order, OrderItem
from products.models import Product
from django.contrib import messages

# Create your views here.

@login_required(login_url='account')
def show_cart(request):
    user = request.user
    customer = user.customer
    cart_items = OrderItem.objects.filter(order__owner=customer, order__order_status=Order.CART_STAGE).order_by('id')
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        # Retrieve user and customer
        user = request.user
        customer = user.customer

        # Retrieve or create the order
        order, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )

        # Retrieve product and quantity from POST data
        product_id = request.POST['product_id']
        product = get_object_or_404(Product, pk=product_id)
        quantity = int(request.POST.get('quantity'))  
        size = request.POST.get('size')

        # Retrieve or create the order item
        order_item, created = OrderItem.objects.get_or_create(
            order=order,
            product=product,
            size=size
        )

        # Update quantity and apply maximum limit
        order_item.quantity = quantity
        order_item.quantity = min(order_item.quantity, 5)  # Apply maximum limit
        order_item.save()

    return redirect('cart')


def remove_from_cart(request, id):
    cart_item = OrderItem.objects.get(id=id)
    cart_item.delete()

    return redirect('cart')


def update_quantity_of_cart_item(request):
    if request.POST:
        cart_item_id = request.POST.get('cart_item_id')
        quantity = int(request.POST.get('quantity'))
        change = int(request.POST.get('change'))
        
        new_quantity = quantity + change
        if 1 <= new_quantity <= 5:
            cart_item = OrderItem.objects.get(id=cart_item_id)
            cart_item.quantity = new_quantity
            cart_item.save()
    
    return redirect('cart')


def checkout(request):
    if request.POST:
        user = request.user
        customer = user.customer
        order = Order.objects.get(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        if order:
            order.set_status(Order.ORDER_CONFIRMED)
            order.total_amount = request.POST.get('total_amount')
            order.save()

            order_items = OrderItem.objects.filter(order=order)
            for order_item in order_items:
                order_item.total_price = order_item.quantity * order_item.product.price
                order_item.save()
            
            # Order Confirmation message
            messages.success(request, 'Your order has been confirmed! Will be processed soon.')

    return redirect('cart')


def orders(request):
    user = request.user
    customer = user.customer
    orders = Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE).order_by('-id')
    return render(request, 'orders.html', {'orders': orders})


def order_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'order.html', {'order': order, 'order_items': order_items})
