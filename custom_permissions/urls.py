from django.urls import path
from .views import CarModelViewset

urlpatterns = [
    path('cv/', CarModelViewset.as_view({'get':'list', 'put':'create'})),
    path('cv/<int:pk>/', CarModelViewset.as_view({'post':'update'}))
]
