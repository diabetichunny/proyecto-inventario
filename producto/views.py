from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, CreateView,
                                  UpdateView, DeleteView,
                                  DetailView, View)

from .utils import render_to_pdf
from datetime import datetime

from producto.models import Suplidor, Producto
from producto.forms import SuplidorForm, ProductoForm


class ProductListView(LoginRequiredMixin, ListView):
    model = Producto
    # paginate_by = 20

    def get_queryset(self):
        result = super(ProductListView, self).get_queryset()

        query = self.request.GET
        values = {}
        for k, v in query.items():
            if v != '':
                if k in ('nombre'):
                    values[k + '__icontains'] = v
                elif k in ('suplidor'):
                    values[k + '__nombre__icontains'] = v
                elif k in ('tipo'):
                    values[k + '__iexact'] = v
                elif k in ('prun_select', 'cant_select'):
                    numeric_value = query['find_' + k[:4]]

                    if numeric_value != '':
                        key = 'cantidad'
                        if k == 'prun_select':
                            key = 'precio_unitario'

                        values[key + '__' + v] = numeric_value

        result = Producto.objects.filter(**values)
        cache.set('productos', result)

        return result

    def dispatch(self, request, *args, **kwargs):
        if not Producto.objects.all():
            return redirect('new_product')
        else:
            return super(ProductListView, self).dispatch(request, *args, **kwargs)


class GenerateProductPDF(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        template = get_template('reporte/reporte_productos.html')

        productos = cache.get('productos', False)

        context = {
            'title': 'Productos',
            'producto_list': productos,
        }
        html = template.render(context)
        pdf = render_to_pdf('reporte/reporte_productos.html', context)

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = 'reporte_productos.pdf'
            content = "attachment; filename='{}'".format(filename)

            response['Content-Disposition'] = content

            return response
        return HttpResponse('Error Generating PDF')


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
    model = Suplidor
    form_class = SuplidorForm


class SupplierListView(LoginRequiredMixin, ListView):
    model = Suplidor

    def get_queryset(self):
        result = super(SupplierListView, self).get_queryset()

        query = self.request.GET
        values = {k + '__icontains': v for k, v in query.items() if v != ''}

        result = Suplidor.objects.filter(**values)
        cache.set('suplidores', result)

        return result

    def dispatch(self, request, *args, **kwargs):
        if not Suplidor.objects.all():
            return redirect('new_supplier')
        else:
            return super(SupplierListView, self).dispatch(request, *args, **kwargs)


class GenerateSupplierPDF(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        template = get_template('reporte/reporte_suplidores.html')

        suplidores = cache.get('suplidores', False)

        context = {
            'title': 'Suplidores',
            'suplidor_list': suplidores,
            'date': datetime.now().date,
        }
        html = template.render(context)
        pdf = render_to_pdf('reporte/reporte_suplidores.html', context)

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = 'reporte_suplidores.pdf'
            content = "attachment; filename='{}'".format(filename)

            response['Content-Disposition'] = content

            return response
        return HttpResponse('Error Generating PDF')


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


@login_required
def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(1, 1, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    return response
