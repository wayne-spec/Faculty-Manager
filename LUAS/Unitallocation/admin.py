from django.contrib import admin
from .models import AcademicYear,School,Course,Semester,UnitType,Unit,Field,Faculty,FacultyType,UnitAllocation,MaxAllocations
# Register your models here

models=[AcademicYear,
    School,
    Course,
    Semester,
    UnitType,
    Unit,
    Field,
    Faculty,
    FacultyType,
    UnitAllocation,
    MaxAllocations,]

for model in models:
    admin.site.register(model)