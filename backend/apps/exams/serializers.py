from rest_framework import serializers

from .models import Exam


class ExamSerializer(serializers.ModelSerializer):
    model = Exam
    fields = "__all__"
