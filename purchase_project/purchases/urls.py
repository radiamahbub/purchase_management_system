from django.urls import path
from purchases.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),


    path('profile/', profile, name='profile'),
    path('profile_update/', profile_update, name='profile_update'),

    # path('supplier/', supplier, name='supplier'),
    # path('supplier_update/', supplier_update, name='supplier_update'),

    path('supplier_add/', supplier_add, name='suppplier_add'),
    path('supplier_list/', supplier_list, name='suppplier_list'),
    path('supplier_update/<str:s_id>/', supplier_update, name='suppplier_update'),
    path('supplier_delete/<str:s_id>/', supplier_delete, name='suppplier_delete'),

    # path('purchase_record/', purchase_record, name='purchase_record'),
    # path('purchase_record_list/', purchase_record_list, name='purchase_record_list'),
    # path('purchase_record_update/<str:p_id>/', purchase_record_update, name='purchase_record_update'),
    # path('purchase_record_delete/<str:p_id>/', purchase_record_delete, name='purchase_record_delete'),
]