from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstApp/', include('firstApp.urls')),
    path('fbvApp/', include('fbvApp.urls')),
    path('cbvApp/', include('cbvApp.urls')),
    path('nsApp/', include('nsApp.urls')),
]
