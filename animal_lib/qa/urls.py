from django.urls import path

#from animal_lib.qa.views import QuestionListView, QuestionAnsListView, QuestionIndexListView, QuestionDetailView
from animal_lib.qa import views
from animal_lib.qa.forms import QuestionForm

app_name = 'qa'

urlpatterns = [
    path("", views.QuestionListView.as_view(), name='index_noans'),
    path("answered/", views.QuestionAnsListView.as_view(), name='index_ans'),
    path("indexed/", views.QuestionIndexListView.as_view(), name='index_all'),
    path("question-detail/<int:pk>/", views.QuestionDetailView.as_view(), name='question_detail'),
    path("ask-question/", views.CreateQuestionView.as_view(form_class=QuestionForm, template_name="qa/question_form.html"), name='ask_question'),
    path("propose-answer/<int:question_id>", views.CreateAnswerView.as_view(), name='propose_answer'),
    path("question/vote/", views.question_vote, name='question_vote'),
    path("answer/vote/", views.answer_vote, name='answer_vote'),
    path("accept-answer/", views.accept_answer, name='accept_answer'),
]
