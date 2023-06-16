from django.shortcuts import render,redirect
from myapp.models import categorydb,productdb
from webapp.models import Registrationdb,Contactusdb,Cartdb,CheckoutDb
from django.contrib import messages


# Create your views here.

def homepage(request):
    data = categorydb.objects.all()
    return render(request,"Home.html",{'data':data})

def aboutpage(request):
    data = categorydb.objects.all()
    return render(request, "aboutpage.html",{'data':data})

def contactpage(request):
    data = categorydb.objects.all()
    return render(request, "contact.html",{'data':data})

def productspage(request,cat_name):
    data = categorydb.objects.all()
    pro = productdb.objects.filter(Category_Name=cat_name)
    prod = productdb.objects.all()
    return render(request,"Products.html",{'data':data, 'pro':pro})

def singleproduct(request,dataid):
    data = categorydb.objects.all()
    pro_single = productdb.objects.get(id=dataid)
    prod = productdb.objects.all()
    return render(request, "SingleProduct.html",{'pro_single':pro_single, 'prod':prod})

def registerpage(request):
    data = categorydb.objects.all()
    return render(request,"RegisterPage.html",{'data':data})

def saveregistration(request):
    if request.method == "POST":
        una = request.POST.get('name')
        ema = request.POST.get('email')
        mob = request.POST.get('mobile')
        img = request.FILES['image']
        pawd = request.POST.get('password')
        obj = Registrationdb(User_Name=una,Email=ema,Mobile=mob,Profile_Image=img,Password=pawd)
        obj.save()
        return redirect(registerpage)




def savelogin(request):
    if request.method == "POST":
        una = request.POST.get('uname')
        pawd = request.POST.get('pass')
        if Registrationdb.objects.filter(User_Name=una,Password=pawd).exists():

            request.session['User_Name']= una
            request.session['Password']= pawd
            messages.success(request, "Login Successfully")
            return redirect(homepage)


        else:
            messages.error(request, "Login Error")
            return redirect(registerpage)
    else:
      messages.error(request, "Login Error")
      return redirect(registerpage)

def UserLogout(request):
    del request.session['User_Name']
    del request.session['Password']
    messages.success(request, "Logout Successful")
    return redirect(registerpage)

def savecontactus(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ema = request.POST.get('email')
        ph = request.POST.get('phone')
        sub = request.POST.get('subject')
        mes = request.POST.get('message')
        obj = Contactusdb(Name=na,Email=ema,Phone=ph,Subject=sub,Message=mes)
        obj.save()
        return redirect(contactpage)

def cartpage(request):
    data = Cartdb.objects.filter(User_Name=request.session['User_Name'])
    return render(request,"cart.html",{'data':data})

def cartsave(request):
    if request.method == "POST":
        una = request.POST.get('uname')
        pna = request.POST.get('pname')
        des = request.POST.get('description')
        prc = request.POST.get('pprice')
        qty = request.POST.get('qty')
        cna = request.POST.get('catname')
        obj = Cartdb(User_Name=una,Product_Name=pna,Description=des,Total_Price=prc,Quantity=qty,Category_Name=cna)
        obj.save()
        return redirect(homepage)

def deletecartitem(request,dataid):
    data = Cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cartpage)

def checkoutpage(request):
    return render(request,"CheckOut.html")

def checkoutsave(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        ema = request.POST.get('email')
        add = request.POST.get('address')
        ph = request.POST.get('phone')
        des = request.POST.get('description')
        obj = CheckoutDb(Name=nam,Email=ema,Address=add,Phone=ph,Description=des)
        obj.save()
        return redirect(homepage)









