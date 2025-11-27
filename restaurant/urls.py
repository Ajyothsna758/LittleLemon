from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'usersview', views.UserViewSet)

urlpatterns=[
    path("", views.index, name="home"),
    path("hello/", views.hello),
    path("users/", views.userView),
]
urlpatterns+= router.urls