from django.shortcuts import render ,redirect
from django.http import HttpResponse
from website.models import user
from django.forms import modelform_factory

curr=None

def start(request):
    if request.method == "POST" :
        login_data = request.POST.dict()
        print(login_data)
        try:
            global curr
            curr= (user.objects.filter(username=f"{login_data['username']}").filter(password=f"{login_data['password']}"))[0]  
        except:
            return render(request,"website/login.html")
        if curr is not None:
            return redirect(f"{curr.role_redirect()}/{curr.username}/")
    else:
        return render(request,"website/login.html")
    

def next(request):
    return HttpResponse("workd!")

user_form=modelform_factory(user,fields=("username","password","email","name"))

def register(request):
    if request.method == "POST" :
        form=user_form(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,"website/register.html",{"form":form})
    else:
        form=user_form()
        return render(request,"website/register.html",{"form":form})


