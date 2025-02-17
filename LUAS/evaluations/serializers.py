from rest_framework import serializers
from .models import EvaluationQuestion, Evaluation, EvaluationResponse


class EvaluationQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationQuestion
        fields = ['id', 'question_text', 'question_type', 'scale_min', 'scale_max']


class EvaluationSerializer(serializers.ModelSerializer):
    questions = EvaluationQuestionSerializer(many=True, read_only=True)  # Add related questions
    question_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=EvaluationQuestion.objects.all(), source='questions'
    )  # For input

    class Meta:
        model = Evaluation
        fields = [
            'id', 'course', 'academicYear', 'unit', 'faculty',
            'created_at', 'Semester', 'questions', 'question_ids'
        ]


class EvaluationResponseSerializer(serializers.ModelSerializer):
    question = EvaluationQuestionSerializer(read_only=True)
    question_id = serializers.PrimaryKeyRelatedField(
        queryset=EvaluationQuestion.objects.all(), source='question'
    )
    evaluation_id = serializers.PrimaryKeyRelatedField(
        queryset=Evaluation.objects.all(), source='evaluation'
    )
    response_text = serializers.CharField(required=False, allow_blank=True)
    response_scale = serializers.IntegerField(required=False)

    class Meta:
        model = EvaluationResponse
        fields = ['id', 'evaluation', 'evaluation_id', 'question', 'question_id', 
                 'response_text', 'response_scale']
        extra_kwargs = {
            'evaluation': {'read_only': True}  # Mark as read-only
        }