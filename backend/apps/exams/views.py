from rest_framework.viewsets import ModelViewSet

from .models import Exam
from .serializers import ExamSerializer


class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Exam.objects.filter(id=user.id).all()

        if user.is_staff:
            queryset = Exam.objects.all()

        return queryset
