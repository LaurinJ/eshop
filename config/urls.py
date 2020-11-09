# import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.home.urls', namespace='home')),
    path('store/', include('app.product.urls', namespace='product')),
    path('cart/', include('app.cart.urls', namespace='cart')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
