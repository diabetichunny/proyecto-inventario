from producto import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index_redirect, name='index'),
    url(r'^nuevo_producto/$', views.CreateProductView.as_view(), name='new_product'),
    url(r'^nuevo_suplidor/$', views.CreateSupplierView.as_view(), name='new_supplier'),
    url(r'^productos/$', views.ProductListView.as_view(), name='product_list'),
    url(r'^productos/(?P<pk>\d+)/(?P<slug>[-\w]+)/$',
        views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^productos/(?P<pk>\d+)/(?P<slug>[-\w]+)/editar/$',
        views.UpdateProductView.as_view(), name='update_product'),
    url(r'^productos/(?P<pk>\d+)/(?P<slug>[-\w]+)/eliminar/$',
        views.DeleteProductView.as_view(), name='delete_product'),
    url(r'^productos/download_pdf/$',
        views.GenerateProductPDF.as_view(), name='download_product_pdf'),
    url(r'^suplidores/$', views.SupplierListView.as_view(), name='supplier_list'),
    url(r'^suplidores/(?P<pk>\d+)/(?P<slug>[-\w]+)/$',
        views.SupplierDetailView.as_view(), name='supplier_detail'),
    url(r'^suplidores/(?P<pk>\d+)/(?P<slug>[-\w]+)/editar/$',
        views.UpdateSupplierView.as_view(), name='update_supplier'),
    url(r'^suplidores/(?P<pk>\d+)/(?P<slug>[-\w]+)/eliminar/$',
        views.DeleteSupplierView.as_view(), name='delete_supplier'),
    url(r'^suplidores/download_pdf/$',
        views.GenerateSupplierPDF.as_view(), name='download_supplier_pdf'),
]
