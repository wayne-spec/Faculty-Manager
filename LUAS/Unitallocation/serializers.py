from django.contrib.auth.models import Group, User
from rest_framework import serializers
from django.utils import timezone
from .models import (
    AcademicYear, School, Course, Semester, UnitType, Unit, Field, 
    Faculty, FacultyType, UnitAllocation, MaxAllocations
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicYear
        fields = ['id', 'academic_year_name', 'start_date', 'end_date', 'created_at', 'updated_at', 'created_by']

class SchoolSerializer(serializers.ModelSerializer):
    director = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    director_username = serializers.CharField(source='director.username', read_only=True)

    class Meta:
        model = School
        fields = ['id', 'school_name', 'director', 'director_username','created_at', 'created_by']


class CourseSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    school_name = serializers.CharField(source="school.school_name", read_only=True)
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'school', 'school_name', 'created_at', 'created_by']


class SemesterSerializer(serializers.ModelSerializer):
    academic_year = serializers.PrimaryKeyRelatedField(queryset=AcademicYear.objects.all())
    academic_year_name = serializers.CharField(source="academic_year.academic_year_name", read_only=True)

    class Meta:
        model = Semester
        fields = ['id', 'semester_name', 'start_date', 'end_date', 'created_at', 'academic_year', 'academic_year_name']


class UnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitType
        fields = ['id', 'service_unit', 'offered_unit']


class UnitSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    unit_type = serializers.PrimaryKeyRelatedField(queryset=UnitType.objects.all())
    school_name = serializers.CharField(source='school.school_name', read_only=True)
    course_name = serializers.CharField(source='course.course_name', read_only=True)
    field = serializers.PrimaryKeyRelatedField(queryset=Field.objects.all())


    class Meta:
        model = Unit
        fields = ['id', 'unit_name', 'unit_short_name', 'unit_code', 'course', 'course_name','field', 'unit_type', 'school', 'school_name','is_on_offer']


class FieldSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    school_name = serializers.CharField(source='school.school_name', read_only=True)

    class Meta:
        model = Field
        fields = ['id', 'field_name', 'field_description', 'school', 'school_name', 'created_at', 'created_by']


class FacultyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyType
        fields = ['id', 'faculty_type_name']


class FacultySerializer(serializers.ModelSerializer):
    field = serializers.PrimaryKeyRelatedField(queryset=Field.objects.all(), many=True)
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    faculty_type = serializers.PrimaryKeyRelatedField(queryset=FacultyType.objects.all())
    school_name = serializers.CharField(source='school.school_name', read_only=True)

    class Meta:
        model = Faculty
        fields = '__all__'

    def create(self, validated_data):
        fields = validated_data.pop('field', [])
        faculty = Faculty.objects.create(**validated_data)
        faculty.field.set(fields)  # Set the many-to-many relationship
        return faculty

    def update(self, instance, validated_data):
        fields = validated_data.pop('field', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        instance.field.set(fields)  # Update the many-to-many relationship
        return instance


class UnitAllocationSerializer(serializers.ModelSerializer):
    unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())
    faculty = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all())
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    semester = serializers.PrimaryKeyRelatedField(queryset=Semester.objects.all())
    academic_year = serializers.PrimaryKeyRelatedField(queryset=AcademicYear.objects.all())
    unit_name = serializers.CharField(source='unit.unit_name', read_only=True)
    course_name = serializers.CharField(source='course.course_name', read_only=True)

    class Meta:
        model = UnitAllocation
        fields = [
            'id', 'unit', 'unit_name', 'faculty', 'course', 'course_name', 
            'semester', 'academic_year', 'allocation_date', 'group'
        ]


class MaxAllocationsSerializer(serializers.ModelSerializer):
    academic_year = serializers.PrimaryKeyRelatedField(queryset=AcademicYear.objects.all())
    faculty_type = serializers.PrimaryKeyRelatedField(queryset=FacultyType.objects.all())
    academic_year_name = serializers.CharField(source='academic_year.academic_year_name', read_only=True)
    faculty_type_name = serializers.CharField(source='faculty_type.faculty_type_name', read_only=True)

    class Meta:
        model = MaxAllocations
        fields = [
            'id', 'academic_year', 'academic_year_name', 'faculty_type', 
            'faculty_type_name', 'max_allocations', 'dead_end_allocations'
        ]



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff']


class GroupSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), source="user_set")

    class Meta:
        model = Group
        fields = ['id', 'name', 'users']
