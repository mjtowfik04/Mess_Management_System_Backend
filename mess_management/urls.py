from django.contrib import admin
from django.urls import path,include
from .views import api_root_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('', api_root_view),
    path('api-auth/', include('rest_framework.urls')),

]
