from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def home(request): 
    name_from_session =  request.session.get("user_name")
    products = Products.get_all()
    print(products)
    return render(request, 'index.html', {"products":products, "usr":name_from_session})

def contact(request):
    if request.method == "GET":
        return render(request, "contact.html")
    else:
        if request.session["user_name"] == None:
            return render(request, 'contact.html',{"msgs":"Please login first to send messages!!"})
        else:
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("msg")

            m = Messages(name=name, email=email, message=message)
            m.save()
            return render(request, 'contact.html',{"msgs":"Message Sent Succesfully!!"})

def about(request):
    return render(request, 'About.html')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get("email")
        psw = request.POST.get("psw")
        
        user = UserLogin.verify_user(email)
        if user:
            if user[0].password == psw:
                print(user[0].name)
                request.session["user_name"] = user[0].name
                return redirect("homepage")
        else:
            err = "user not foung"
            return render(request, "login.html", {"err":"Invalid Email or Password!!"})
            print("not found") 


def logout(request):
    request.session["user_name"] = None
    return redirect("homepage")