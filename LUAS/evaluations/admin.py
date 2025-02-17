from django.contrib import admin
from .models import EvaluationQuestion, Evaluation, EvaluationResponse
# Register your models here.

models = [EvaluationQuestion, Evaluation, EvaluationResponse]

for model in models:
    admin.site.register(model)

