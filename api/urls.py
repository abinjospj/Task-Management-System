from django.urls import path
from users import views as UserViews
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from tasks.views import Tasks, TaskDetail

urlpatterns = [
    path('register/', UserViews.RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('tasks/', Tasks.as_view(), name='tasks'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]