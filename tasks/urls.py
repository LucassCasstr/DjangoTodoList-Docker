from django.urls import path

from . import views

urlpatterns = [
    path('',views.tasks, name='tasks'),
    path('teste/',views.teste, name='teste'),
    path('newtask/', views.newTask, name="new-task"),
    path('editar/', views.editar, name="editar"),
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
]