from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Exam:
    exam_name = models.CharField(max_length=255)
    total_marks = models.IntegerField(null=True)
    total_number_of_questions = models.IntegerField(null=True, default=0)
    time_duration = models.IntegerField(null=True, default=0)
    marks_for_correct_choice = models.IntegerField(null=True)
    marks_for_incorrect_choice = models.IntegerField(null=True)
    question = models.IntegerField(null=True)
    user = models.ForeignKey(User, related_name="exam", on_delete=models.CASCADE)

    def __str__(self):
        return self.exam_name

    class Meta:
        db_table = "exam"
        ordering = ("-id", )
