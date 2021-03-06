from django.conf.urls import url
from InfOrquidea import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^genero$',views.generoApi),
    url(r'^genero/([0-9]+)$',views.generoApi),

    url(r'^especie$',views.especieApi),
    url(r'^especie/([0-9]+)$',views.especieApi),

    url(r'^familiaDeOrquideas$',views.familiaDeOrquideaApi),
    url(r'^familiaDeOrquideas/([0-9]+)$',views.familiaDeOrquideaApi),

    url(r'^usuario$',views.usuarioApi),
    url(r'^usuario/([0-9]+)$',views.usuarioApi),

    url(r'^orquidea$',views.orquideaApi),
    url(r'^orquidea/([0-9]+)$',views.orquideaApi)
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)