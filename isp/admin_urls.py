from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', admin.site.urls), # Admin is now at the root of admin.isp-qq06.onrender.com
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)