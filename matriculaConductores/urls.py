from django.urls import path,include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    #url app |
    path('', include('web.urls')),
    #url api
    path('', include('api.urls')),


    #
    path('accounts/', include('django.contrib.auth.urls'))

]
