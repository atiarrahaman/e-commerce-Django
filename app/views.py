from django.shortcuts import render
from .models import Product
from django.views import View


class ProductView(View):
    def get(self, request):
        mobaile=Product.objects.filter(category='m')
        topw=Product.objects.filter(category='tw')
        contex={'m':mobaile,'tw':topw}
        return render(request, 'app/home.html',contex)


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class product_detailView(View):
    def get(self , request, id):
        product= Product.objects.get(id=id)
        context={'product':product}

        return render(request, 'app/productdetail.html',context)


def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
    if data==None:
        mobaile=Product.objects.filter(category='m')
    elif data=='Redmi' or data== 'Samsung' or data== 'Vivo':
        mobaile=Product.objects.filter(category='m').filter(brand=data)
    elif data=='below' :
        mobaile=Product.objects.filter(category='m').filter(discount_price__lt=10000)
    elif data=='upto' :
        mobaile=Product.objects.filter(category='m').filter(discount_price__gt=10000)
    context={'m':mobaile}
    return render(request, 'app/mobile.html',context)
def Laptop(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
