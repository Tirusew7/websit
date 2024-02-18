
from django.contrib import admin
from django.urls import path
from product.views import home, about, contact, product
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('product/', product)
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
