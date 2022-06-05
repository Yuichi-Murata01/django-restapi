from django.urls import path, include
from rest_framework import routers
from api.views import TaskViewSet, TagViewSet

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('tag', TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]