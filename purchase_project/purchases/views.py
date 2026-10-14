from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from purchases.forms import *
from purchases.models import *


# Create your views here.

def dashboard(request):

    return render(request, 'purchases/dashboard.html')

def profile(request):

    context = {
        'title':'Profile',
    }

    return render(request, 'purchases/profile.html', context)

def profile_update(request):

    current_user = request.user

    try:
        profile_data = request.user_profile
    except:
        profile_data = None    


    form = UserProfileForm(instance=profile_data)

    if request.method == 'POST':

        form = UserProfileForm(request.POST, request.FILES, instance=profile_data)

        if form.is_valid():

            user = form.save(commit=False)

            form.save()

            return redirect('profile')

    context = {
            'title':'Profile',
            'form_title':'Profile Update Form',
            'form_btn':'Update',
            'form':form
        }
    
    return render(request, 'form_base.html', context)



# def supplier(request):

#     context = {
#         'title':'Supplier',
#     }

#     return render(request, 'purchases/supplier.html', context)

# def supplier_update(request):

#     current_user = request.user

#     try:
#         supplier_data = request.supplier_profile
#     except:
#         supplier_data = None    


#     form = SupplierForm(instance=supplier_data)

#     if request.method == 'POST':

#         form = SupplierForm(request.POST, request.FILES, instance=supplier_data)

#         if form.is_valid():

#             user = form.save(commit=False)

#             form.save()

#             return redirect('supplier')

#     context = {
#             'title':'supplier',
#             'form_title':'supplier Update Form',
#             'form_btn':'Update',
#             'form':form,
#             'supplier_data':'supplier_data'
#         }
    
#     return render(request, 'form_base.html', context)


def supplier_add(request):

    supplier_name = request.POST.get('supplier_name')
    contact_number = request.POST.get('contact_number')
    address = request.POST.get('address')

    if request.method == "POST":

        s_data = SupplierModel.objects.create(
            supplier_name = supplier_name,
            contact_number = contact_number,
            address = address,
        )

        


    return render(request, 'purchases/supplier_add.html')

def supplier_list(request):

    return render(request, 'purchases/supplier_list.html')

def supplier_update(request):

    return render(request, 'purchases/supplier_update.html')

def supplier_delete(request):

    return render(request, 'purchases/supplier_delete.html')
