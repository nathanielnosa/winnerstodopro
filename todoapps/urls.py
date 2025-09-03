from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.TodoView.as_view()),
    path('gettodos/',views.TodoView.as_view()),
    path('gettodo/<str:id>/',views.DetailTodoView.as_view()),
    path('updatetodo/<str:id>/',views.DetailTodoView.as_view()),
    path('deletetodo/<str:id>/',views.DetailTodoView.as_view()),
]