from django.urls import path

from .views.person_view import PersonApiView

urlpatterns = [
    path('api/person', PersonApiView.as_view())
]
