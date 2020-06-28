from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.home,name="home"),
    path('products/', views.product,name="products"),
    path('customer/<str:pk>', views.customer ,name="customer"),

    path('login/', views.Login ,name="login"),
    path('logout_user/',views.logoutUser,name="logout"),
    path('register/', views.register ,name="register"),

    path('create/order/<str:pk>',views.make_form,name="make_form"),
    path('makee_order/<str:pk>',views.make_form_12,name="make_form_12"),
    path('user/',views.user_page,name="user_page"),

    path('update_order/<str:pk>',views.update_form,name="update_form"),
    path('delete_order/<str:pk>',views.deleteOrder,name="delete_form"),
    path('delete_order/<str:customerId>/<str:pk>', views.deleteOrder, name="delete_form_customer")
]
