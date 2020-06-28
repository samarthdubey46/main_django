from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import models, login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import OrderForm, CreateUserForm
from .filter import OrderFilter

@login_required(login_url='login')
def home(request):
    order = Order.objects.all()
    CUstomer = Customer.objects.all()
    to = order.count()
    dv = order.filter(status="Delivered").count()
    pn = order.filter(status="Pending").count()
    d = {"order": order, "customer": CUstomer, "delivered": dv, "total": to, "pending": pn}

    return render(request, 'accounts/dashboard.html', d)

@login_required(login_url='login')
def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

@login_required(login_url='login')
def customer(request, pk):
    c_by_id = Customer.objects.get(id=pk)
    orders = c_by_id.order_set.all()
    td = orders.all().count()
    filtter = OrderFilter(request.GET, queryset=orders)
    orders = filtter.qs

    d = {"customer": c_by_id, "order": orders, "total": td, "filter": filtter}

    return render(request, 'accounts/customer.html', d)

@login_required(login_url='login')
def make_form(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('Product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    # form = OrderForm(initial={"customer":customer})
    form_set = OrderFormSet(instance=customer)
    if request.method == "POST":
        # form = OrderForm(request.POST)
        form_stt = OrderFormSet(request.POST, instance=customer)
        if form_stt.is_valid():
            form_stt.save()
            return redirect('home')

    context = {"form": form_set, "customer": customer}
    return render(request, 'accounts/form_update.html', context)

@login_required(login_url='login')
def update_form(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/form_update.html', context)

@login_required(login_url='login')
def make_form_12(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('Product', 'status'), extra=5)
    customer1 = Customer.objects.get(id=pk)
    # form = OrderForm(initial={"customer":customer})
    form_set = OrderFormSet(queryset=Order.objects.none(), instance=customer1)
    if request.method == "POST":
        # form = OrderForm(request.POST)
        form_stt = OrderFormSet(request.POST, instance=customer1)
        if form_stt.is_valid():
            form_stt.save()
            return redirect('home')

    context = {"form": form_set, "customer": customer}
    return render(request, 'accounts/make_forms_1.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk, customerId=None):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order, 'customer': customerId}
    return render(request, 'accounts/delete.html', context)

@unauthenticated_user
def Login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username Or Password is Incorrect")

    context = {}
    return render(request, 'accounts/Login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f"{user} Has been Sucessfully Registered")

            return redirect('login')
    context = {"form": form}
    return render(request, 'accounts/register.html', context)
def user_page(request):
    context = {}
    return render(request,'accounts/user_profile.html',context)

# Create your views here.
