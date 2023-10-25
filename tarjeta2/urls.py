from django.urls import path , include
from rest_framework import routers
from .views import Tarjeta2View

router = routers.DefaultRouter()
router.register(r'tarjeta2', Tarjeta2View)

urlpatterns = [
    path('', include(router.urls)) ,
]
