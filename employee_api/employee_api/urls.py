from django.contrib import admin
from django.urls import path, include
from backend.views import frontend  # ✅ Make sure to import this view

urlpatterns = [
    path('', frontend),  # Renders frontend.html
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),  # DRF API endpoints
]
