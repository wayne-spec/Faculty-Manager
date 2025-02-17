from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone

# AuditMixin to include auditing fields
class AuditMixin(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, related_name="%(class)s_created_by", default=1)
    updated_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, related_name="%(class)s_updated_by", null=True, blank=True, default=None)

    class Meta:
        abstract = True

# Models

class AcademicYear(AuditMixin):
    academic_year_name = models.CharField(max_length=255, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("Start date must be before end date.")

    def __str__(self):
        return self.academic_year_name



class School(AuditMixin):
    school_name = models.CharField(max_length=255, unique=True, default="School of Computing and Engineering Sciences")
    director = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.school_name

class Course(AuditMixin):
    course_name = models.CharField(max_length=255, unique=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

class Semester(AuditMixin):
    semester_name = models.CharField(max_length=255, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("Start date must be before end date.")

    def __str__(self):
        return self.semester_name

class UnitType(models.Model):
    service_unit = models.BooleanField(default=False)
    offered_unit = models.BooleanField(default=False)

    def __str__(self):
        return "Offered Unit" if self.offered_unit else "Service Unit"
    
class Field(AuditMixin):
    field_name = models.CharField(max_length=255)
    field_description = models.CharField(max_length=255, default="Researcher in Machine Learning/Machine Learning Engineer")
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.field_name


class Unit(AuditMixin):
    unit_name = models.CharField(max_length=255)
    unit_short_name = models.CharField(max_length=50)
    unit_code = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    unit_type = models.ForeignKey(UnitType, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, editable=False)
    field = models.ForeignKey(Field,on_delete=models.CASCADE,default=1)
    is_on_offer = models.BooleanField(default=False, help_text="Is the unit on offer?")

    def save(self, *args, **kwargs):
        if self.course and self.course.school:
            self.school = self.course.school  # Automatically set the school based on the course
        super().save(*args, **kwargs)

    def __str__(self):
        return self.unit_name



class FacultyType(models.Model):
    faculty_type_name = models.CharField(max_length=100, unique=True, default="Full-Time")

    def __str__(self):
        return self.faculty_type_name

class Faculty(AuditMixin):
    staff_number = models.IntegerField(unique=True, default=166937)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    address = models.TextField()
    date_of_birth = models.DateField()
    field = models.ManyToManyField(Field)
    profile_link = models.URLField(blank=True, null=True)
    religion = models.CharField(max_length=255, blank=True, null=True)
    joining_date = models.DateField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    faculty_type = models.ForeignKey(FacultyType, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class UnitAllocation(AuditMixin):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    allocation_date = models.DateField()
    group = models.CharField(max_length=20, default="Group A")
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.faculty} - {self.unit} - {self.group} ({self.semester})"

class MaxAllocations(AuditMixin):
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    faculty_type = models.ForeignKey(FacultyType, on_delete=models.CASCADE)
    max_allocations = models.PositiveIntegerField()
    dead_end_allocations = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.faculty_type} - Max: {self.max_allocations}, Dead-end: {self.dead_end_allocations}"
