from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView

# Cart
from .models import Category, Product, LogoSectionProduct
from django.contrib.auth.decorators import login_required
from cart.cart import Cart



class index(TemplateView):
  template_name ="web/index.html" 
   
  def get_context_data(self, **kwargs) :
      context = super().get_context_data(**kwargs)
      context["categories"] = Category.objects.all()
      context["product"] = Product.objects.all()
      context["ProuctLogo"] = LogoSectionProduct.objects.all()
      context["display_categories"] = Category.objects.filter(display_in_home=True)
      return context
  
class detail_page(DetailView):
  template_name ="web/detail_page.html" 
  model = Product




def checkout(request):
  return render(request, 'web/checkout.html')


def login(request):
  return render(request, 'web/accounts/login.html')



def register(request):
    return render (request,'web/accounts/register.html') 


def success(request):
  return render(request, 'web/success.html')





@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'web/cart_detail.html')

