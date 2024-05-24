from django.contrib import admin
from django.urls import path

import engine

urlpatterns = [
    path('admin/', admin.site.urls),
    path('erniebot/', engine.erniebotturbo),
]
