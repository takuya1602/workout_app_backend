from django.db import models
from django.conf import settings


class Target(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    target = models.ForeignKey(
        Target, on_delete=models.PROTECT, related_name="exercise"
    )

    def __str__(self):
        return self.name


class Workout(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Set(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent_workout = models.ForeignKey(
        Workout, on_delete=models.CASCADE, related_name="sets"
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_NULL, null=True)
    weight = models.IntegerField()
    reps = models.IntegerField()
