from django.urls import path , include
from rest_framework import routers
from .views import Tarjeta1View

router = routers.DefaultRouter()
router.register(r'tarjeta1', Tarjeta1View)

urlpatterns = [
    path('', include(router.urls)) ,
]
