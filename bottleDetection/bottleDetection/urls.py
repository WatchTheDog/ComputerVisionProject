from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('index.urls')),
    path('impressum/', include('impressum.urls')),
    path('datenschutz/', include('datenschutz.urls')),
    path('admin/', admin.site.urls),
]

