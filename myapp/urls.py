from django.urls import path
from myapp import views

urlpatterns = [
path('indexpage/',views.indexpage,name="indexpage"),
path('addcategory/',views.addcategory,name="addcategory"),
path('savecategory/',views.savecategory,name="savecategory"),
path('displaycategory/',views.displaycategory,name="displaycategory"),
path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
path('updatecategorydata/<int:dataid>/',views.updatecategorydata,name="updatecategorydata"),
path('deletecategory/<int:dataid>/',views.deletecategory,name="deletecategory"),
path('addproduct/',views.addproduct,name="addproduct"),
path('saveproduct/',views.saveproduct,name="saveproduct"),
path('productdisplay/',views.productdisplay,name="productdisplay"),
path('editproduct/<int:dataid>/',views.editproduct,name="editproduct"),
path('updateproductdata/<int:dataid>/',views.updateproductdata,name="updateproductdata"),
path('deleteproduct/<int:dataid>/',views.deleteproduct,name="deleteproduct"),
path('adminloginpage/',views.adminloginpage,name="adminloginpage"),
path('adminlogin/',views.adminlogin,name="adminlogin"),
path('adminlogout/',views.adminlogout,name="adminlogout"),
path('displaycontact/',views.displaycontact,name="displaycontact"),
path('deletecontact/<int:dataid>/',views.deletecontact,name="deletecontact"),



]