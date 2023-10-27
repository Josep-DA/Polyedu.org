from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication-related URLs
    path('', include('polyedu.urls')),
    path('polynews/', include('polynews.urls')),
    path('polyshop/', include('polyshop.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('polyedu/', include('polyedu.urls')),
)