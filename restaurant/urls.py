from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'usersview', views.UserViewSet)
router.register(r'tables', views.BookingView)

urlpatterns=[
    path("", views.index, name="home"),
    path("hello/", views.hello),
    path("users/", views.userView),
    path("menu/", views.MenuItemView.as_view(), name="menu"),
    path("menu/<int:pk>/", views.SingleMenuItemView.as_view()),
]
urlpatterns+= router.urls