# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from pybo.models import Question, Answer


# 요청이 되어 이 함수가 실행된 것이니 request써주기
def index(request):
    """
    pybo 목록 출력
    """
    # -기호가 붙어있으면 역방향, 없으면 순방향 (게시물을 최신순으로 보기 떄문에 작성일시의 역순(-)으로 정렬)
    question_list = Question.objects.order_by('-create_date') # Question 전체에 대해서 질문등록일시를 역순(-)으로 정렬한 것을 question_list 객체에 넣어줌
    context = {'question_list': question_list} #foreach문과 비슷?
    return render(request, 'pybo/question_list.html', context)
    # render는 데이터를 내가 가지고 있는 템플릿에 적용시켜서 html로 보여주는 함수


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    # 답변 등록시 텍스트창에 입력한 내용은 answer_create 함수의
    # 첫번째 매개변수 request를 통해 읽을 수 있음
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    answer.save()
    return redirect('pybo:detail', question_id=question.id)
    # 답변등록 후 질문 상세 화면을 다시 보여주기 위해 redirect 함수 사용
    # redirect 함수는 페이지 이동을 위한 함수
    # detail 별칭은 question_id가 필요하므로 question.id를 인수로 전달함