"""notePyReact URL Configuration


"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/notes/', include('notes.urls')),
    # url(r'^api-auth/', include('rest_framework.urls'))
]
