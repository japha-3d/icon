from django.shortcuts import render, get_object_or_404
from ecommerce_website.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import OrderItem, Order, Product
from .forms import OrderCreateForm
from cart.views import get_cart, cart_clear
from decimal import Decimal
def order_create(request):
    cart = get_cart(request)
    cart_qty = sum(item['quantity'] for item in cart.values())
    transport_cost =50
    if request.method == 'POST':
        order_form = OrderCreateForm(request.POST)
        if order_form.is_valid():
            cf = order_form.cleaned_data
            transport = cf['transport']
            email=cf['email']
            first_name=cf['first_name']
            last_name=cf['last_name']
            telephone=cf['telephone']
            #adress=cf['adress']
            if transport == 'Recipient pickup':
                transport_cost = 0
            order = order_form.save(commit=False)
            order.transport_cost = Decimal(transport_cost)
            order.save()
            
            product_ids = cart.keys()
            products = Product.objects.filter(id__in=product_ids)
            for product in products:
                cart_item =cart[str(product.id)]
                price=eval(cart_item['price'])
                quantity=(cart_item['quantity'])
                total=(price*quantity)+50
                OrderItem.objects.create(order=order,product=product,price=cart_item['price'],quantity=cart_item['quantity'])
                subject = f'Order number is {order.id}'
                
                message = f'Name: {first_name}{last_name} \nTelephone: {telephone}\nproduct: {product}\nQuantity: {quantity}\nprice: {price}\nDelivery_Charges: 50\nTotal_Bill: {total}'
                recepient_list = ['huzaifaafzal259@gmail.com']
                send_mail(subject, 
                message, EMAIL_HOST_USER, recepient_list, fail_silently = False)

            cart_clear(request)
            return render(
            request,
            'order_created.html',
            {'order': order}
            )
    else:
        order_form = OrderCreateForm()
    return render(
    request,'order_create.html',{'cart':cart,'order_form':order_form,'transport_cost':transport_cost,}
    )