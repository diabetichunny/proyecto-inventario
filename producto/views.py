from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView,
                                  DetailView)

from producto.models import Suplidor, Producto
from producto.forms import SuplidorForm, ProductoForm


class ProductListView(LoginRequiredMixin, ListView):
    # login_url = '/login/'
    # redirect_field_name = 'producto/product_list.html'
    model = Producto

    def dispatch(self, request, *args, **kwargs):
        if not Producto.objects.all():
            return redirect('new_product')
        else:
            return super(ProductListView, self).dispatch(request, *args, **kwargs)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Producto


class UpdateProductView(LoginRequiredMixin, UpdateView):
    form_class = ProductoForm
    model = Producto
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('product_list')


class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('product_list')


class CreateProductView(LoginRequiredMixin, CreateView):
    def dispatch(self, request, *args, **kwargs):
        if not Suplidor.objects.all():
            return redirect('new_supplier')
        else:
            return super(CreateProductView, self).dispatch(request, *args, **kwargs)

    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('product_list')


class CreateSupplierView(LoginRequiredMixin, CreateView):
    # login_url = '/login/'
    # redirect_field_name = 'producto/product_list.html'
    model = Suplidor
    form_class = SuplidorForm


class SupplierListView(LoginRequiredMixin, ListView):
    # login_url = '/login/'
    # redirect_field_name = 'producto/supplier_list.html'
    model = Suplidor

    def dispatch(self, request, *args, **kwargs):
        if not Suplidor.objects.all():
            return redirect('new_supplier')
        else:
            return super(SupplierListView, self).dispatch(request, *args, **kwargs)


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Suplidor


class UpdateSupplierView(LoginRequiredMixin, UpdateView):
    form_class = SuplidorForm
    model = Suplidor
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('supplier_list')


class DeleteSupplierView(LoginRequiredMixin, DeleteView):
    model = Suplidor
    success_url = reverse_lazy('supplier_list')


# ---------------------------------------------------- FBV ----------------------------------------------------

def index_redirect(request):
    return HttpResponseRedirect(reverse('product_list'))


# @login_required
# def
