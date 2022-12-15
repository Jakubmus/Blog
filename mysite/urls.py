from django.contrib import admin
from django.urls import include, path
from app.views import base, read

urlpatterns = [
    path('', base, name='base'),
    path('admin/', admin.site.urls),
    path('<int:id>/', read, name='read'),
]
