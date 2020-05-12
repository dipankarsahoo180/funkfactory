from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib import admin

admin.site.site_header = 'Funk Factory Dance Studio'                           # default: "Django Administration"
admin.site.index_title = 'Funk Factory administration'                           # default: "Site administration"
admin.site.site_title = 'FUNK FACTORY DANCE STUDIO'

urlpatterns = [
    path('', views.home),
]