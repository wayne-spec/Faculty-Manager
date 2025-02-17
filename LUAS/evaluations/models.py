from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from Unitallocation.models import Course, Unit, Faculty, AcademicYear, Semester
from django.core.exceptions import ValidationError


# Model for Evaluation Questions
class EvaluationQuestion(models.Model):
    SCALE = 'scale'
    COMMENT = 'comment'
    QUESTION_TYPES = [
        (SCALE, 'Scale'),
        (COMMENT, 'Comment'),
    ]

    question_text = models.TextField()
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    scale_min = models.IntegerField(null=True, blank=True)
    scale_max = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.question_text


# Model for Evaluations
class Evaluation(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    academicYear = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, default=1)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=1)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    Semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=1)
    questions = models.ManyToManyField(EvaluationQuestion, related_name="evaluations")

    def __str__(self):
        return f"Evaluation for {self.unit} ({self.course}, Academic Year {self.academicYear}, Semester {self.Semester})"

    def get_questions_with_responses(self):
        """
        Returns all questions with their corresponding responses for the evaluation.
        If a response does not exist for a question, it will return None for the response.
        """
        questions = self.questions.all()
        responses = {response.question_id: response for response in self.responses.all()}
        return [{"question": question, "response": responses.get(question.id)} for question in questions]


# Model for Evaluation Responses
class EvaluationResponse(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, related_name="responses")
    question = models.ForeignKey(EvaluationQuestion, on_delete=models.CASCADE, related_name="responses")
    response_text = models.TextField(null=True, blank=True)  # For comment-based questions
    response_scale = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True  # For scale-based questions
    )

    class Meta:
        unique_together = ('evaluation', 'question')

    def clean(self):
        # Custom validation to make sure either response_text or response_scale is provided
        if self.question.question_type == 'scale' and not self.response_scale:
            raise ValidationError(f"Scale response is required for the question: {self.question}")
        elif self.question.question_type == 'comment' and not self.response_text:
            raise ValidationError(f"Comment response is required for the question: {self.question}")

    def __str__(self):
        return f"Response to {self.question} in {self.evaluation}"