from django.urls import path, include
from rest_framework import routers
from api.views import TaskViewSet, TagViewSet, MessageViewSet

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('tags', TagViewSet)
router.register('Messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls))
]