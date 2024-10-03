from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from kars import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kars.urls')),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
]

# Add this to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
