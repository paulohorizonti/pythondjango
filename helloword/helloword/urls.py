from django.urls.conf import include
from django.contrib import admin
from django.urls import path


from . import views
app_name = 'website'
urlpatterns = [
    #Inclui as URLs do app ‘website’
    path('', include('website.urls', namespace='website')),
    # Interface administrativa
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
]
