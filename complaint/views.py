from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Topic, SubTopic, Question, Answer, Anyother
# from .tasks import send_feedback_email_task


@api_view(['GET', 'POST'])
def index(request):
    name = request.data['name']
    email = request.data['email']
    # data = User.objects.all().values()
    # for i in data:
    #     if i.get('name') == name and i.get('email') == email:
    #         return HttpResponseRedirect(redirect_to="http://127.0.0.1:8000/complaint/topics/")
    obj = {
        "name": name,
        "email": email
    }
    # User.objects.create(name=name, email=email)
    # User.save()
    return Response({"msg": obj})


@api_view(['GET', 'POST'])
def topics(request):
    tid = request.GET.get('q')
    sid = request.GET.get('q2')
    qid = request.GET.get('q3')

    if qid and sid and tid:
        qid = int(qid)
        data = Answer.objects.filter(question_id=qid).values()
        # print(data[0].get('answer'))
        send_feedback_email_task.delay(
            data[0].get('answer')
        )
        return Response({"Answer": data[0].get('answer')})

    elif sid and tid:
        sid = int(sid)
        data = Question.objects.all().values()
        d = {}
        for i in data:
            # print(i)
            if i.get('subtopic_id') == sid:
                d[i.get('id')] = i.get('question')
        return Response({"Questions": d})

    elif tid:
        tid = int(tid)
        if tid == 6:
            new_topic = request.data
            new_question = new_topic['required_topic']
            all_data = Anyother.objects.all().values()
            for i in all_data:
                if i.get('question') == new_question:
                    return Response({"msg": i.get('answer')})
            anyother = Anyother.objects.create(question=new_question, answer="It will be resolved at the earliest.")
            anyother.save()
            return Response({"msg": "We will get back to you regarding this shortly!"})
        data = SubTopic.objects.all().values()
        # print(data)
        d = {}
        for i in data:
            # print(i)
            if i.get('topic_id') == tid:
                # print(i.get('subtopic'))
                d[i.get('id')] = i.get('subtopic')
        return Response({"Sub Topics": d})

    else:
        data = Topic.objects.all().values()
        # print(data)
        d = {}
        for i in data:
            # print(i)
            d[i.get('id')] = i.get('topic')
        return Response({"Topics": d})
