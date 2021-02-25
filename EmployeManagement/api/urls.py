from django.urls import include, path
from rest_framework import routers
from management import views



router = routers.DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]