from django.urls import path
from .views import InvoiceListView, InvoiceCreateView, InvoiceUpdateView, InvoiceDeleteView

urlpatterns = [
    path('', InvoiceListView.as_view(), name='invoice-list'),
    path('create/', InvoiceCreateView.as_view(), name='invoice-create'),
    path('<int:pk>/edit/', InvoiceUpdateView.as_view(), name='invoice-edit'),
    path('<int:pk>/delete/', InvoiceDeleteView.as_view(), name='invoice-delete'),
]
