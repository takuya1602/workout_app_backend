from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import Target, Exercise, Workout, Set

class SetInline(NestedStackedInline):
  model = Set
  extra = 1


class WorkoutAdmin(NestedModelAdmin):
  model = Workout
  inlines = [SetInline]

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Exercise)
admin.site.register(Target)