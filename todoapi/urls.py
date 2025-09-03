from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('owolariboy/', admin.site.urls),
    path('api/',include('todoapps.urls'))
]
