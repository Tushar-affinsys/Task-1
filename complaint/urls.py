from .viewsets import TopicViewSet, SubTopicViewSet, QuestionViewSet, AnswerViewSet, AnyotherViewSet
from django.urls import path
from rest_framework.routers import SimpleRouter
from complaint import views, viewsets

router = SimpleRouter()
router.register("topic", viewset=TopicViewSet, basename='Topic')
router.register("subtopic", viewset=SubTopicViewSet, basename='SunTopic')
router.register("question", viewset=QuestionViewSet, basename='Question')
router.register("answer", viewset=AnswerViewSet, basename='Answer')
router.register("anyother", viewset=AnyotherViewSet, basename='Answer')


urlpatterns = [
    path('', views.index),
    path('topics/', views.topics),
    # path('topics/<int:id>/', views.sub_topics),
    # path('topics/<int:tid>/<int:sid>/', views.questions),
    # path('topics/<int:tid>/<int:sid>/<int:qid>/', views.answers),

]
urlpatterns += router.urls
