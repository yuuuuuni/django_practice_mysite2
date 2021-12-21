# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import QuestionForm
from .models import Question, Answer


# 요청이 되어 이 함수가 실행된 것이니 request써주기
def index(request):
    """
    pybo 목록 출력
    """
    # -기호가 붙어있으면 역방향, 없으면 순방향 (게시물을 최신순으로 보기 떄문에 작성일시의 역순(-)으로 정렬)
    question_list = Question.objects.order_by(
        '-create_date')  # Question 전체에 대해서 질문등록일시를 역순(-)으로 정렬한 것을 question_list 객체에 넣어줌
    context = {'question_list': question_list}  # 자바의 맵 같은것 {'키':값}
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


def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':  # 요청 방식이 POST 이면
        form = QuestionForm(request.POST)  # 그 값을(request.POST은 사용자가 입력한 폼) form 이라는 변수에 저장
        if form.is_valid():  # 그 form이라는 변수가 유효하다면
            question = form.save(commit=False)  # form 변수를 임시저장해서 question이라는 변수에 넣기
            question.create_date = timezone.now()  # question의 등록날짜를 등록 시점으로 해라
            question.save()  # 저장해라
            return redirect('pybo:index')  # 첫번쨰 화면인 질문 목록의 화면으로 이동해라
    else:  # get 방식이면
        form = QuestionForm() # 빈칸으로 해도 무방
    context = {'form': form}  # {키:값}
    return render(request, 'pybo/question_form.html', context)

