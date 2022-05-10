from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('detektivka.urls')),
    path('admin/', admin.site.urls),
]
