from django.shortcuts import render, HttpResponse, redirect
from django.forms import modelform_factory
from website.models import products
def menu(request,username):
    return render(request,"manager/menu.html")
# Create your views here.

product_form =modelform_factory(products,exclude=[])

def newProduct(request):
    if request.method == "POST" :
        form=product_form(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('menu')
        else:
            return render(request,"manager/new_product.html",{"form":form})
    else:
        form=product_form()
        return render(request,"manager/new_product.html",{"form":form})

