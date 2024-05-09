from django.urls import include, path
from rest_framework import routers
from students import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'grades', views.GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

