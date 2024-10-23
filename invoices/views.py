from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Invoice
from .forms import InvoiceForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator

@login_required(login_url="/users/login/")
def invoice_list(request):
    invoice_queryset = Invoice.objects.all()
    

    paginator = Paginator(invoice_queryset, 10)
    
    page_number = request.GET.get('page', 1)
    
   
    invoice_page = paginator.get_page(page_number)
    
    return render(request, "invoices/invoice_list.html", {"invoices": invoice_page})


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
