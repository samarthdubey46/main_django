from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home,name="home"),
    path('products/', views.product,name="products"),
    path('customer/<str:pk>', views.customer ,name="customer"),

    path('account/', views.accountSettings, name="account"),

    path('login/', views.Login ,name="login"),
    path('logout_user/',views.logoutUser,name="logout"),
    path('register/', views.register ,name="register"),

    path('create/order/<str:pk>',views.make_form,name="make_form"),
    path('make_order/<str:pk>',views.make_form_12,name="make_form_12"),
    path('user/',views.user_page,name="user_page"),

    path('update_order/<str:pk>',views.update_form,name="update_form"),
    path('delete_order/<str:pk>',views.deleteOrder,name="delete_form"),
    path('delete_order/<str:customerId>/<str:pk>', views.deleteOrder, name="delete_form_customer"),

    path('reset_password/',auth_view.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name="reset_password"),
    path('reset_password_sent/',auth_view.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),name="password_reset_confirm"),
    path('reset_password_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_sent.html'),name="password_reset_complete"),
]
