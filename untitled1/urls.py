
from django.contrib import admin
from django.urls import path,include
from accounts import urls
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls))
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
