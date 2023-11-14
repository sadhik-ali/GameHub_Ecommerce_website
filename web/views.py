from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Category, Product, LogoSectionProduct, gamecartsection, gamecartsectiontwo
# Create your views here.
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from cart.cart import Cart


class index(TemplateView):
  template_name ="web/index.html" 
   
  def get_context_data(self, **kwargs) :
      context = super().get_context_data(**kwargs)
      context["categories"] = Category.objects.all()
      context["product"] = Product.objects.all()
      context["ProuctLogo"] = LogoSectionProduct.objects.all()
      context["display_categories"] = Category.objects.filter(display_in_home=True)
      return context
  
class Detail_Page(DetailView):
  template_name ="web/Detail_Page.html" 
  model = Product



class game(TemplateView):
  template_name ="web/game.html" 
   
  def get_context_data(self, **kwargs) :
      context = super().get_context_data(**kwargs)
      context["gamecartfirst"] = gamecartsection.objects.all()
      context["gamecartsecond"] = gamecartsectiontwo.objects.all()
      
      return context
  

def checkout(request):
  return render(request, 'web/checkout.html')


def login(request):
  return render(request, 'web/account/login.html')


def signup(request):
  return render(request, 'web/account/signup.html')


def success(request):
  return render(request, 'web/success.html')


def cart_detail(request):
    return render(request, 'web/cart_detail.html')

