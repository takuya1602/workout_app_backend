from rest_framework import generics

from .models import Target, Exercise, Workout
from .serializers import TargetSerializer, WorkoutSerializer, ExerciseSerializer


class TargetList(generics.ListCreateAPIView):
    serializer_class = TargetSerializer

    def get_queryset(self):
        return Target.objects.filter(user=self.request.user)


class ExerciseList(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        return Exercise.objects.filter(user=self.request.user)


class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        return Exercise.objects.filter(user=self.request.user)


class WorkoutList(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)


class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)
