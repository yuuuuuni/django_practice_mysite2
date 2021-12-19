from django.contrib import admin
from .models import Question, Answer

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject'] # 관리자의 Qusetion 화면에서 제목으로 검색할 수 있도록 해줌

admin.site.register(Question, QuestionAdmin) # Question 모델을 관리자에 등록해주는 명령어


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['content'] # 관리자의 Answer 화면에서 답변 내용으로 검색할 수 있게 해줌

admin.site.register(Answer, AnswerAdmin) # Answer 모델을 관리자에 등록해주는 명령어