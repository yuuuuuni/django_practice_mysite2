from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject # 제목을 표시할 수 있게 해줌


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 질문에 대한 답변에 해당하므로 Question 모델을 속성으로 가져가야함
    # 기존 모델을 속성으로 연결하려면 ForeignKey 사용
    # on_delete=models.CASCADE 의 의미는 이 답변과 연결된 질문(Question)이 삭제되면 답변(Answer)도 삭제된다는 뜻
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content # 내용을 표시할 수 있게 해줌



