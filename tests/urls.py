
from django.urls import path, include
from .views import IndexView, CreateView, TestDetailView, QuestionView, ConfirmView, AttemptView, SuccessView, DashboardView, ResponsesView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('responses', ResponsesView.as_view(), name='responses'),
    path('create', CreateView.as_view(), name='create'),
    path('test_detail', TestDetailView.as_view(), name='test_detail'),
    path('question', QuestionView.as_view(), name='question'),
    path('confirm', ConfirmView.as_view(), name='confirm'),
    path('attempt/<user_identifier>/<test_identifier>', AttemptView.as_view(), name='attempt'),
    path('attempt/<user_identifier>/<test_identifier>/<accept>', AttemptView.as_view(), name='accept_attempt'),
    path('attempt/<user_identifier>/<test_identifier>/<accept>/<con>', AttemptView.as_view(), name='con_attempt'),
    path('success', SuccessView.as_view(), name='success')
    
]