from django.urls import path
from cast.api.views import PersonCreateAPIView, PersonDetailAPIView

urlpatterns = [
    path("People/",
        PersonCreateAPIView.as_view(),
        name="People-list"),

    path("Person/<int:pk>/",
        PersonDetailAPIView.as_view(),
        name="job-detail")
]