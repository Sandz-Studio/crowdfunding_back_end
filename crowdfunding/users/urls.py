from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view(), name='customuser-list'),
    path('users/<int:pk>/', views.CustomUserDetail.as_view(), name='customuser-detail'),
    # path("session/", views.SessionUserDetailView.as_view(), name="session"),
]