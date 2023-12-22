from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('product_detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('error404/', views.error404, name='error404'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)