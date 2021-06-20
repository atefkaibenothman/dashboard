from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.views import ActorView, FilmView

router = routers.DefaultRouter()
router.register(r"actors", ActorView, "actor")
router.register(r"films", FilmView, "film")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("dashboard/", include("frontend.urls")),
]
