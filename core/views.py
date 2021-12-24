from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def data_edit(request, pk, model, title_page, button_text, redirect_url):
    entity = model.objects.get(id=pk)
    form_custom = get_custom_form(model, '__all__')
    if request.method == 'POST':
        form = form_custom(request.POST, instance=entity)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_custom(instance=entity)
    context = {
        'entity': entity,
        'form': form,
        'title_page': title_page,
        'button_text': button_text,
        'redirect_url': redirect_url
    }
    return render(request, 'core/edit.html', context)


@login_required(login_url='auth-login')
def data_delete(request, pk, model, title_page, button_text, redirect_url):
    entity = model.objects.get(id=pk)
    if request.method == 'POST':
        entity.delete()
        return redirect(redirect_url)
    context = {
        'entity': entity,
        'title_page': title_page,
        'button_text': button_text,
        'redirect_url': redirect_url
    }
    return render(request, 'core/delete.html', context)

@login_required(login_url='auth-login')
def data_method(request, model, title_page, button_text, redirect_url, column_list, add_form=True):
    
    entity = model.objects.all()
    entity_no = entity.count()

    if request.method == 'POST':
        form_custom = get_custom_form(model, '__all__')
        form = form_custom(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else: 
        form = get_custom_form(model, '__all__')
    context = {
        'entity': entity,
        'form': form,
        'entity_count': entity_no,
        'title_page': title_page,
        'button_text': button_text,
        'add_form': add_form,
        'column_list': column_list,
        'redirect_url': redirect_url,
    }

    return render(request, 'core/board.html', context)

@login_required(login_url='auth-login')
def index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    shipment = Shipment.objects.all()
    shipment_count = shipment.count()
   
    context = {
        'order': order,
        'product': product,
        'shipment': shipment,
        'product_count': product_count,
        'order_count': order_count,
        'shipment_count': shipment_count,
    }
    return render(request, 'core/index.html', context)

@login_required(login_url='auth-login')
def employees(request):
    return data_method(request, User, 'Employees', 'Add Employees', 'core-employees', User._meta.fields, False)

@login_required(login_url='auth-login')
def products(request):
    return data_method(request, Product, 'Products', 'Add Product', 'core-products', Product._meta.fields)

@login_required(login_url='auth-login')
def orders(request):
    return data_method(request, Order, 'Orders', 'Add Order', 'core-orders', Order._meta.fields)

@login_required(login_url='auth-login')
def product_edit(request, pk):
    return data_edit(request, pk, Product, 'Product', 'Edit Product', 'core-products')

@login_required(login_url='auth-login')
def product_delete(request, pk):
    return data_delete(request, pk, Product, 'Product', 'Delete Product', 'core-products')

@login_required(login_url='auth-login')
def order_edit(request, pk):
    return data_edit(request, pk, Order, 'Order', 'Edit Order', 'core-orders')

@login_required(login_url='auth-login')
def order_delete(request, pk):
    return data_delete(request, pk, Order, 'Order', 'Delete Order', 'core-orders')

@login_required(login_url='auth-login')
def clients(request):
    return data_method(request, OrderClient, 'Clients', 'Add Client', 'core-clients', OrderClient._meta.fields)

@login_required(login_url='auth-login')
def client_edit(request, pk):
    return data_edit(request, pk, OrderClient, 'Client', 'Edit Client', 'core-clients')

@login_required(login_url='auth-login')
def client_delete(request, pk):
    return data_delete(request, pk, OrderClient, 'Client', 'Delete Client', 'core-clients')

@login_required(login_url='auth-login')
def vendors(request):
    return data_method(request, Vendor, 'Vendors', 'Add Vendor', 'core-vendors', Vendor._meta.fields)

@login_required(login_url='auth-login')
def vendor_edit(request, pk):
    return data_edit(request, pk, Vendor, 'Vendor', 'Edit Vendor', 'core-vendors')

@login_required(login_url='auth-login')
def vendor_delete(request, pk):
    return data_delete(request, pk, Vendor, 'Vendor', 'Delete Vendor', 'core-vendors')

@login_required(login_url='auth-login')
def categories(request):
    return data_method(request, Category, 'Categories', 'Add Category', 'core-categories', Category._meta.fields)

@login_required(login_url='auth-login')
def category_edit(request, pk):
    return data_edit(request, pk, Category, 'Category', 'Edit Category', 'core-categories')

@login_required(login_url='auth-login')
def category_delete(request, pk):
    return data_delete(request, pk, Vendor, 'Category', 'Delete Category', 'core-categories')

@login_required(login_url='auth-login')
def contracts(request):
    return data_method(request, Contract, 'Contracts', 'Add Contract', 'core-contracts', Contract._meta.fields)

@login_required(login_url='auth-login')
def contract_edit(request, pk):
    return data_edit(request, pk, Contract, 'Contract', 'Edit Contract', 'core-contracts')

@login_required(login_url='auth-login')
def contract_delete(request, pk):
    return data_delete(request, pk, Contract, 'Contract', 'Delete Contract', 'core-contracts')

@login_required(login_url='auth-login')
def shipments(request):
    return data_method(request, Shipment, 'Shipments', 'Add Shipment', 'core-shipments', Shipment._meta.fields)

@login_required(login_url='auth-login')
def shipment_edit(request, pk):
    return data_edit(request, pk, Shipment, 'Shipment', 'Edit Shipment', 'core-shipments')

@login_required(login_url='auth-login')
def shipment_delete(request, pk):
    return data_delete(request, pk, Shipment, 'Shipment', 'Delete Shipment', 'core-shipments')

@login_required(login_url='auth-login')
def payments(request):
    return data_method(request, PaymentMethod, 'Payments', 'Add Payment', 'core-payments', PaymentMethod._meta.fields)

@login_required(login_url='auth-login')
def payment_edit(request, pk):
    return data_edit(request, pk, PaymentMethod, 'Payment', 'Edit Payment', 'core-payments')

@login_required(login_url='auth-login')
def payment_delete(request, pk):
    return data_delete(request, pk, PaymentMethod, 'Payment', 'Delete Payment', 'core-payments')

@login_required(login_url='auth-login')
def series(request):
    return data_method(request, Series, 'Series', 'Add Series', 'core-series', Series._meta.fields)

@login_required(login_url='auth-login')
def series_edit(request, pk):
    return data_edit(request, pk, Series, 'Series', 'Edit Series', 'core-series')

@login_required(login_url='auth-login')
def series_delete(request, pk):
    return data_delete(request, pk, Series, 'Series', 'Delete Series', 'core-series')
