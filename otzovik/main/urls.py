from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import transport as qr
urlpatterns = [
    path('', views.home, name='home'),
    path('transport/', views.transport, name='transport'),
    path('personal/', views.personal, name='personal'),
    path('support/', views.support, name='support'),
    path('anketa/', views.anketa, name ='anketa'),
    path('bay/', qr, name='bay'),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)