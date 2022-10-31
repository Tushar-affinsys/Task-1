from django.db import models


class Topic(models.Model):
    topic = models\
        .CharField(default="", max_length=100)


class SubTopic(models.Model):
    subtopic = models.CharField(max_length=100, default="")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default="")


class Question(models.Model):
    question = models.CharField(max_length=100, default="")
    subtopic = models.ForeignKey(SubTopic, on_delete=models.CASCADE, default="")


class Answer(models.Model):
    answer = models.CharField(max_length=100, default="")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default="")


class Anyother(models.Model):
    question = models.CharField(max_length=100, default="")
    answer = models.CharField(max_length=100, default="")


# class User(models.Model):
#     name = models.CharField(max_length=100, default="")
#     email = models.EmailField()
