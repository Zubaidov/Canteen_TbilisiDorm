from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('reservation/', views.reservation, name='reservation'),
    path('blogs/', views.blogs, name='blogs'),
    path('contact/', views.contact, name='contact'),
    path('error404/', views.error404, name='error404'),
    path('menu/', views.menu, name='menu'),
    path('product/<int:id>', views.productSingle, name='productSingle'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)