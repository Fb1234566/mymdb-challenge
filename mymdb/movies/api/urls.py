from django.urls import path
from movies.api.views import CharacterCreateAPIView, CharacterDetailAPIView

urlpatterns = [
    path("Characters/",
        CharacterCreateAPIView.as_view(),
        name="People-list"),

    path("Character/<int:pk>/",
        CharacterDetailAPIView.as_view(),
        name="job-detail")
]