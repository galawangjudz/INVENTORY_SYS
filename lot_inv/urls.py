from django.http.response import StreamingHttpResponse
from django.urls import path
from django.conf import settings
from django.urls.resolvers import URLPattern
from . import views 
from django.conf.urls.static import static

app_name = 'lot_inv'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('lots', views.lots, name = 'lot-inv'),
    path ('add_lot/', views.add_lot, name = 'add_lot'),
    path ('update_lot/<str:pk>/', views.update_lot, name = 'update_lot'),
    path ('delete_lot/<str:pk>/', views.delete_lot, name = 'delete_lot'),
    path('generate_lid', views.generate_lid, name = 'generate_lid'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)