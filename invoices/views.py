from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Invoice
from .forms import InvoiceForm
from django.urls import reverse_lazy

class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoices/invoice_list.html'

class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoices/invoice_form.html'
    success_url = reverse_lazy('invoice-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = self
        context['view'].action = 'Create'
        return context

class InvoiceUpdateView(UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoices/invoice_form.html'
    success_url = reverse_lazy('invoice-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = self
        context['view'].action = 'Update'
        return context

class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'invoices/invoice_confirm_delete.html'
    success_url = reverse_lazy('invoice-list')
