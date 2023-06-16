from django.shortcuts import render,redirect
from myapp.models import categorydb,productdb
from webapp.models import Contactusdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.

def indexpage(request):
    return render(request,"index.html")
def addcategory(request):
    return render(request, "AddCategory.html")

def savecategory(request):
    if request.method == "POST":
        cna = request.POST.get('name')
        des = request.POST.get('description')
        cimg = request.FILES['image']
        obj = categorydb(Category_Name=cna,Description=des,Category_Image=cimg)
        obj.save()
        messages.success(request, "Category Saved Successfully")
        return redirect(addcategory)

def displaycategory(request):
    data = categorydb.objects.all()
    return render(request,"DisplayCategory.html",{'data':data})

def editcategory(request,dataid):
    data = categorydb.objects.get(id=dataid)
    return render(request,"EditCategory.html",{'data':data})

def updatecategorydata(request,dataid):
    if request.method == "POST":
        cna = request.POST.get('name')
        des = request.POST.get('description')
        try:
            cimg = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(cimg.name,cimg)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).Category_Image
        categorydb.objects.filter(id=dataid).update(Category_Name=cna,Description=des,Category_Image=file)
        return redirect(displaycategory)

def deletecategory(request,dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)

def addproduct(request):
    data = categorydb.objects.all()
    return render(request,"AddProduct.html",{'data':data})

def saveproduct(request):
    if request.method == "POST":
        cat = request.POST.get('category')
        pna = request.POST.get('pname')
        prc = request.POST.get('price')
        des = request.POST.get('description')
        bra = request.POST.get('brand')
        pimg = request.FILES['image']
        obj = productdb(Category_Name=cat,Product_Name=pna,Price=prc,Description=des,Brand=bra,Product_Image=pimg)
        obj.save()
        messages.success(request, "Product Saved Successfully")
        return redirect(addproduct)

def productdisplay(request):
    data = productdb.objects.all()
    return render(request,"DisplayProduct.html",{'data':data})

def editproduct(request,dataid):
    category = categorydb.objects.all()
    data = productdb.objects.get(id=dataid)
    return render(request,"EditProduct.html",{'data':data,'category':category})

def updateproductdata(request,dataid):
    if request.method == "POST":
        cat = request.POST.get('category')
        pna = request.POST.get('pname')
        prc = request.POST.get('price')
        des = request.POST.get('description')
        bra = request.POST.get('brand')
        try:
            pimg = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(pimg.name,pimg)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Product_Image
        productdb.objects.filter(id=dataid).update(Category_Name=cat,Product_Name=pna,Price=prc,Description=des,Brand=bra,Product_Image=file)
        return redirect(productdisplay)

def deleteproduct(request,dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(productdisplay)

def adminloginpage(request):
    return render(request, "AdminLogin.html")

def adminlogin(req):
    if req.method == "POST":
        uname = req.POST.get('username')
        pswrd = req.POST.get('password')
    if User.objects.filter(username__contains=uname).exists():
        user = authenticate(username=uname, password=pswrd)

        if user is not None:
            login(req,user)
            req.session['username']= uname
            req.session['password']= pswrd
            messages.success(req, "Login Successfully")
            return redirect(indexpage)
        else:
            messages.error(req, "Login Error")
            return redirect(adminloginpage)
    else:
        messages.error(req, "Login Error")
        return redirect(adminloginpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout Successful")
    return redirect(adminloginpage)

def displaycontact(request):
    data = Contactusdb.objects.all()
    return render(request, "DisplayContactpage.html",{'data':data})

def deletecontact(request,dataid):
    data = Contactusdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontact)









