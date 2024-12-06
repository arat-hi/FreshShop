from django.urls import path,include
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('',views.loginUser,name='loginUser'),
    path('home',views.view_product,name='home'),
    path('addCart/<int:id>',views.AddCart,name='addCart'),
    path('viewCart',views.viewCart,name="viewCart"),
    path('deleteCart/<int:id>',views.cartDelete,name="deleteCart"),
    path('logout',views.logoutUser,name="logout")
]