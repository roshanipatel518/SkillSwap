from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

def api_info(request):
    return JsonResponse({
        'message': 'SkillSwap API',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': {
            'auth': '/api/auth/',
            'users': '/api/users',
            'requests': '/api/requests',
            'notifications': '/api/notifications',
            'admin_api': '/api/admin/',
            'admin_panel': '/admin/'
        }
    })

@csrf_exempt
def health_check(request):
    return JsonResponse({'status': 'ok', 'message': 'Backend is running'})

urlpatterns = [
    path('', api_info, name='api_info'),
    path('health/', health_check, name='health_check'),
    path('admin/', admin.site.urls),
    path('api/', include('requests.urls')),
    path('api/', include('notifications.urls')),
    path('api/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
