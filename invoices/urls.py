from django.urls import path
from .views import invoice_list, InvoiceCreateView, InvoiceUpdateView, InvoiceDeleteView

urlpatterns = [
    path('', view=invoice_list, name='invoice-list'),
    path('create/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('<int:pk>/edit/', InvoiceUpdateView.as_view(), name='invoice-edit'),
    path('<int:pk>/delete/', InvoiceDeleteView.as_view(), name='invoice-delete'),
]
