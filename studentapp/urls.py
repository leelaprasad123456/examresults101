from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('admin_login/', views.admin_login, name='admin-login'),
    path('admin_panel/', views.admin_panel, name='admin-panel'),
    path('delete-student/<int:id>/', views.delete_student, name='delete-student'),
    path('edit-student/<int:id>/', views.edit_student, name='edit-student'),
    path('edit-confirm/<int:id>/', views.edit_confirm, name='edit-confirm'),
    path('logout/', views.admin_logout, name='admin-logout'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_confirm/', views.add_confirm, name='add_confirm'),
]
