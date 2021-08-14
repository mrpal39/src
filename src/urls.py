
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('allauth/',include('allauth.urls')),
    path('',include('accounts.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns +=[



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'accounts.views.error_404_view'
