from django.urls import path
from .views import PersonList, PersonDetail

urlpatterns = [
    path('people/', PersonList.as_view(), name="person-list"),
    path('people/<int:pk>/', PersonDetail.as_view(), name="person-detail"),
]
