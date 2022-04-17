from dataclasses import field
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import Target, Exercise, Workout, Set


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = (
            "exercise",
            "weight",
            "reps",
        )


class WorkoutSerializer(WritableNestedModelSerializer):
    sets = SetSerializer(many=True)

    class Meta:
        model = Workout
        fields = (
            "id",
            "title",
            "created_at",
            "sets",
        )
