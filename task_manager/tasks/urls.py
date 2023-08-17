from django.urls import path
from task_manager.tasks.views import TaskView, \
    TaskShowView, TaskDestroyView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path('', TaskView.as_view(), name='tasks_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/delete/', TaskDestroyView.as_view(), name='task_delete'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/', TaskShowView.as_view(), name='task_show'),
]
