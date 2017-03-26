from django.contrib import admin
from .models import TutionCentre, Tutor, Student
# Register your models here.
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(TutionCentre)
