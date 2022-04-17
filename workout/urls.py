from django.urls import path
from .views import WorkoutList, WorkoutDetail, ExerciseList, ExerciseDetail, TargetList

urlpatterns = [
    path("workouts/", WorkoutList.as_view()),
    path("workouts/<int:pk>/", WorkoutDetail.as_view()),
    path("exercises/", ExerciseList.as_view()),
    path("exercises/<int:pk>", ExerciseDetail.as_view()),
    path("targets/", TargetList.as_view()),
]
