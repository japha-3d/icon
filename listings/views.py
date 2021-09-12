from django.db.models import query
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product,Review,Contact
from .forms import ReviewForm
from cart.forms import CartAddProductForm
from django.views.generic import DetailView
def product_list(request, category_slug=None):
    categories = Category.objects.all()
    requested_category = None
    products = Product.objects.all()

    if category_slug:
        requested_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=requested_category)
    else:
        requested_category=None
        products=Product.objects.all()

    return render(
        request,
        'product/list.html',
        {
            'categories': categories,
            'requested_category': requested_category,
            'products': products
        }
    )


    category=get_object_or_404(Category,slug=category_slug)
    product=get_object_or_404(Product,category_id=category.id,slug=product_slug)
    if request.method=="POST":
        review_form=ReviewForm(request.POST)
        if review_form.is_valid():
            cf=review_form.cleaned_data
            author_name="Anonymous"
            Review.objects.create(product=product,author=author_name,rating=cf['rating'],text=cf['text'])
            return redirect('listings:product_detail',category_slug=category_slug,product_slug=product_slug)
    else:
        review_form = ReviewForm()
        cart_product_form = CartAddProductForm()

        return render(
            request,
            'product/detail.html',
            {
                'product': product,
                'review_form': review_form,
                'cart_product_form': cart_product_form
            }
        )


    return render(
        request,'product/detail.html',{'product':product,'review_form':review_form})
class Detail(DetailView):
    model=Product
    template_name="product/detail.html"
def List(request):
    categories=Category.objects.all()

    return render(request,'product/list2.html',{"categories":categories})
def Add(request):
    categories=Category.objects.all()
    if request.method=="POST":
        name = request.POST.get("name")
        images=request.FILES.getlist('image')
        category=Category.objects.get(id=request.POST.get("category"))
        for image in images:
            ins=Product(name=name,image=image,category=category)
            ins.save()
        return redirect("/")
        
            
    return render(request,'product/add.html',{'categories':categories})
def Search(request):
    query=request.GET['query']
    categories=Category.objects.filter(name__icontains=query)
    return render(request,"product/search_packets.html",{"categories":categories})
def Search_icons(request):
    japha=request.GET['japha']
    products=Product.objects.filter(name__icontains=japha)
    return render(request,"product/search_icons.html",{'products':products})
def Contact_us(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        ins=Contact(name=name,email=email,message=message)
        ins.save()
        return redirect('/')
    return render(request,'product/contact.html')
def about(request):
    return render(request,"product/about.html")
def policy(request):
    return render(request,'product/policy.html')
