from django.urls import path , include
from rest_framework import routers
from .views import Tarjeta3View

router = routers.DefaultRouter()
router.register(r'tarjeta3', Tarjeta3View)

urlpatterns = [
    path('', include(router.urls)) ,
]
