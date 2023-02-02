from django.contrib import admin
from django.urls import path, include
from projectapp import views as projectappViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', projectappViews.home, name='home'),
    path('base/', projectappViews.base, name='base'),
    path('accounts/', include('accounts.urls')),
    path('pricing/', projectappViews.pricing, name='pricing'),
    path('pricing/payment/', projectappViews.payment, name='payment'),
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)