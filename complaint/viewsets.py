from rest_framework import viewsets
from .models import Topic, SubTopic, Question, Answer, Anyother
from .serializers import TopicSerializer, SubTopicSerializer, QuestionSerializer, AnswerSerializer, AnyotherSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class SubTopicViewSet(viewsets.ModelViewSet):
    queryset = SubTopic.objects.all()
    serializer_class = SubTopicSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnyotherViewSet(viewsets.ModelViewSet):
    queryset = Anyother.objects.all()
    serializer_class = AnyotherSerializer
