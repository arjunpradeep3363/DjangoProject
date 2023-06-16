from django.urls import path
from webapp import views




urlpatterns = [

 path('homepage/',views.homepage,name="homepage"),
 path('aboutpage/',views.aboutpage,name="aboutpage"),
 path('contactpage/',views.contactpage,name="contactpage"),
 path('singleproduct/<int:dataid>/',views.singleproduct,name="singleproduct"),
 path('productspage/<cat_name>', views.productspage, name="productspage"),
 path('registerpage/', views.registerpage, name="registerpage"),
 path('saveregistration/', views.saveregistration, name="saveregistration"),
 path('savelogin/', views.savelogin, name="savelogin"),
 path('UserLogout/', views.UserLogout, name="UserLogout"),
 path('savecontactus/', views.savecontactus, name="savecontactus"),
 path('cartpage/', views.cartpage, name="cartpage"),
 path('cartsave/', views.cartsave, name="cartsave"),
 path('deletecartitem/<int:dataid>/',views.deletecartitem,name="deletecartitem"),
 path('checkoutpage/',views.checkoutpage,name="checkoutpage"),
 path('checkoutsave/',views.checkoutsave,name="checkoutsave"),

]