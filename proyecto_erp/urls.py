from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.svg', permanent=True)),
    path('admin/', admin.site.urls),
    # Set the dashboard as the homepage
    path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    
    # Include other app URLs
    path('ventas/', include('ventas.urls', namespace='ventas')),
    path('compras/', include('compras.urls', namespace='compras')),
    path('productos/', include('productos.urls', namespace='productos')),
    path('contabilidad/', include('contabilidad.urls', namespace='contabilidad')),
    path('agenda/', include('agenda.urls', namespace='agenda')),
    path('calendario/', include('calendario.urls', namespace='calendario')),
    path('calculadora/', include('calculadora.urls', namespace='calculadora')),
    path('hoja_calculo/', include('hoja_calculo.urls', namespace='hoja_calculo')),
    path('notas/', include('notas.urls', namespace='notas')),
    
    # Add path for logout view
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    
    # Include auth URLs - only include these once
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Personalizar títulos del admin
admin.site.site_header = "Administración del ERP"
admin.site.site_title = "ERP Admin"
admin.site.index_title = "Panel de Administración"
